from typing import Any, Dict, Set, TypeVar

import numpy as np
import torch

T = TypeVar("T")
Tensor = torch.Tensor
Array = np.ndarray[Any, Any]

class OneHotEncodedPersistenceDiagram(Tensor):
    """This class represents a single one-hot encoded persistence diagram.
    """
    def __init__(self, *args, **kwargs):  # type: ignore
        super().__init__(*args, **kwargs)
        self._check_if_valid()
    
    def get_num_homology_dimensions(self) -> int:
        """This method returns the number of homology dimensions.
        """
        return self.shape[-1] - 2
    
    def get_num_points(self) -> int:
        """This method returns the number of points.
        """
        return self.shape[0]
    
    def __repr__(self):
        return (f"OneHotEncodedPersistenceDiagram({self.shape})"
                f" with {self.get_num_homology_dimensions()} homology dimensions:"
                f" and {self.shape[2]} number of points and the data:"
                f" {self.data}, {self.device}")
    
    def _check_if_valid(self) -> None:
        if self.ndimension() != 2:
            raise ValueError("The input should be a 2-dimensional tensor."
                                f"The input has {self.ndimension()} dimensions.")
        assert self.shape[-1] > 2, \
            "The input should have at least one homology dimensions."
        assert torch.all(self[:, 2:] >= 0) and \
            torch.all(self[:, 2:].sum(dim=1) == 1.0), \
                "The homology dimension should be one-hot encoded."
                

def get_one_hot_encoded_persistence_diagram_from_gtda(persistence_diagram: Array) \
    -> OneHotEncodedPersistenceDiagram:
    """This function takes a single persistence diagram from giotto-tda and returns a one-hot encoded
    persistence diagram.
    
    Args:
        persistence_diagram: An array of shape (num_points, 3) where the first two columns
                                represent the coordinates of the points and the third column
                                represents the index of the homology dimension.
        
    Returns:
        A one-hot encoded persistence diagram. If the persistence diagram has only one homology
        dimension, the third column will be filled with ones.
    """
    assert persistence_diagram.ndim == 2 and persistence_diagram.shape[1] >=2, \
        "The input should be a 2-dimensional array of shape (num_points, 3) or (num_points, 2)."

    if persistence_diagram.shape[1] == 2:
        return OneHotEncodedPersistenceDiagram(
            torch.stack((torch.tensor(persistence_diagram),
                         torch.ones(persistence_diagram.shape[0])), dim=1))
    else:
        homology_types: Set[int] = set([int(i) for i in persistence_diagram[:, 2]])
        type_to_one_hot_encoding: Dict[int, int] = {
            i: j for j, i in enumerate(homology_types)
        }
        one_hot_encoding: Tensor = torch.zeros(persistence_diagram.shape[0],
                                                len(homology_types))
        # TODO: Fill the one-hot encoding in a vectorized manner.
        for i, j in enumerate(persistence_diagram[:, 2]):
            one_hot_encoding[i, type_to_one_hot_encoding[int(j)]] = 1
        birth_death_diagram: Tensor = torch.tensor(persistence_diagram[:, :2])
            
        return OneHotEncodedPersistenceDiagram(
            torch.stack((birth_death_diagram,
                         one_hot_encoding), dim=1))
