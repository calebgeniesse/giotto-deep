from typing import List, Tuple, Union
# deep learning
import torch
import numpy as np
from torch import nn

from ..analysis.decision_boundary import \
    UniformlySampledPoint,\
    GradientFlowDecisionBoundaryCalculator

# plot
import plotly.express as px
import pandas as pd

# ML
from sklearn.metrics import pairwise_distances

Tensor = torch.Tensor
Array = np.ndarray


class Compactification:
    """Class to compactify the feature space and get
    better topological insights.

    Args:
        precision :
            A tolerance on how close to the decision
            boundary the points shall be.
        n_features :
            number of input features
        n_samples:
            number of samples per chart
        n_epochs:
            number of epochs needed to push points to the
            decison boundary
        boundary_tuple :
            list of pairs (left,right).
            This list defines the boundaries in each coordinates
        neural_net :
            the trained network of which to compute
            the boundary
    """

    def __init__(self, precision: float = 0.4,
                 n_features: int = None,
                 n_samples: int = 1000,
                 epsilon: float = 0.05,
                 n_epochs: int = 5000,
                 boundary_tuple: List[Tuple[float, float]] = None,
                 neural_net: nn.Module = None) -> None:

        if n_features is None:
            raise ValueError("Need to specify the number of features.")
        else:
            self.n_features = n_features
        if neural_net is None:
            raise ValueError("Need to specify the trained network.")
        else:
            self.neural_net = neural_net
        if boundary_tuple is None:
            self.boundary_tuple = [(-1., 1.) for _ in range(self.n_features)]
        else:
            self.boundary_tuple = boundary_tuple
        self.precision = precision
        self.n_samples = n_samples
        self.epsilon = epsilon
        self.n_epochs = n_epochs
        self.patches = None
        self.list_of_pts_in_patches = None
        self.label_final = None
        self.check_compute_charts = False

    @staticmethod
    def _transition_to_patch(sample_points_tensor: Tensor, i: int) -> Union[Tensor, Array]:
        stacking_list = []
        if i == -1:
            points = sample_points_tensor
            return points
        else:
            for dim in range(sample_points_tensor.shape[1]):
                if dim == i:
                    stacking_list.append(1/sample_points_tensor[:, dim])
                else:
                    stacking_list.append(sample_points_tensor[:, dim] /
                                         sample_points_tensor[:, i])
            if type(sample_points_tensor) == Tensor:
                return torch.stack(stacking_list, dim=1)
            return np.stack(stacking_list, axis=1)

    def _compute_charts(self) -> List[Tensor]:
        # compute boundary
        self.patches = []

        # loop over patches
        for i in range(-1, self.n_features):
            # print(i)
            # sample pts uniformly to 0-th patch
            sample_points = UniformlySampledPoint(self.boundary_tuple,
                                                  n_samples=self.n_samples)
            plot_points_tensor = torch.from_numpy(sample_points()).float()
            # move to i-th patch
            sample_points_tensor = self._transition_to_patch(plot_points_tensor, i)

            # Using new gradient flow implementation
            gf = GradientFlowDecisionBoundaryCalculator(model=self.neural_net,
                                                        initial_points=sample_points_tensor,
                                                        optimizer=lambda params:
                                                        torch.optim.Adam(params))
            gf.step(number_of_steps=self.n_epochs)
            res = gf.get_filtered_decision_boundary(delta=self.precision).detach().cpu()
            # back to 0-th patch
            plot_points_tensor = self._transition_to_patch(res, i)
            self.patches.append(plot_points_tensor)
        self.check_compute_charts = True
        return self.patches

    def create_final_distance_matrix(self) -> Tuple[Array, List]:
        """This is the main function to call without arguments"""
        if self.check_compute_charts is False:
            self._compute_charts()
        self.list_of_pts_in_patches = []
        for i in range(len(self.patches)):
            list_of_pts_per_patch = []
            for j, pts in enumerate(self.patches):
                if j == i:
                    list_of_pts_per_patch.append(pts)
                else:
                    list_of_pts_per_patch.append(self._transition_to_patch(
                        self._transition_to_patch(pts, j-1), i-1))
            self.list_of_pts_in_patches.append(np.concatenate(list_of_pts_per_patch))

        list_of_distances = []
        for array in self.list_of_pts_in_patches:
            list_of_distances.append(pairwise_distances(array))

        d_patch = np.stack(list_of_distances, axis=2)
        d_final = np.min(d_patch, axis=2)
        self.label_final = []
        for j, patch in enumerate(self.patches):
            self.label_final += list(j*np.ones(len(patch)))
        return d_final, self.label_final

    def plot_chart(self, i: int) -> None:
        """This functions plots the points in each chart.

        Args:
            i :
                the chart index, from ``-1`` to ``n_features``
        """
        df_plot = pd.DataFrame(self.list_of_pts_in_patches[i], columns=["x" + str(j) for j in
                               range(self.list_of_pts_in_patches[i].shape[1])])
        df_plot["label"] = self.label_final
        if self.list_of_pts_in_patches[i].shape[1] == 2:
            fig = px.scatter(df_plot, x="x0", y="x1", color='label')
            fig.show()
        elif self.list_of_pts_in_patches[i].shape[1] >= 3:
            fig = px.scatter_3d(df_plot, x="x0", y="x1", z="x2", color='label')
            fig.show()
