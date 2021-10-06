import numpy as np
import torch
from ...optimisation import PersistenceGradient


def test_PersistenceGradient_2d():
    '''check if the class is consistent.
    '''
    X = torch.tensor([[1, 0.], [0, 1.], [2, 2], [2, 1]])
    hom_dim = (0, 1)
    pg = PersistenceGradient(homology_dimensions=hom_dim,
                             zeta=0.1,
                             max_edge_length=3,
                             collapse_edges=True)
    assert X.dtype == torch.float32
    assert pg.phi(X).shape[0] == 14
    assert (np.array([[0,  4], [1,  5],
            [2,  6], [3, -1], [-1, -1],
            [-1, -1], [-1, -1], [-1, -1]]) == pg._persistence(X)[0]).all()
    assert pg.persistence_function(X).item() >= -2.328427314758301 - 0.001
    pg.SGD(X, n_epochs=4, lr=0.4)


def test_PersistenceGradient_3d():
    '''check if the class is consistent.
    '''
    X = torch.tensor([[1, 0., 1], [0, 1., 0], [2, 2, 1], [2, 1, 2]])
    hom_dim = (0, 1)
    pg = PersistenceGradient(homology_dimensions=hom_dim,
                             zeta=0.1,
                             max_edge_length=3,
                             collapse_edges=True)
    assert X.dtype == torch.float32
    assert pg.phi(X).shape[0] == 14
    assert (np.array([[0,  4], [1,  5],
            [2,  6], [3, -1], [-1, -1],
            [-1, -1], [-1, -1], [-1, -1]]) == pg._persistence(X)[0]).all()
    assert pg.persistence_function(X).item() >= -2.7783148288726807 - 0.001
    pg.SGD(X, n_epochs=4, lr=0.4)


def test_PersistenceGradient_5d():
    '''check if the class is consistent.
    '''
    X = torch.tensor([[1, 0., 1, 0.5, 1], [0, 1., 0, 0.5, 1],
                      [2, 2, 1, 0.5, 1], [2, 1, 2, 0.5, 1]])
    hom_dim = (0, 1)
    pg = PersistenceGradient(homology_dimensions=hom_dim,
                             zeta=0.1,
                             max_edge_length=3,
                             collapse_edges=True)
    assert X.dtype == torch.float32
    assert pg.phi(X).shape[0] == 14
    assert (np.array([[0,  4], [1,  5],
            [2,  6], [3, -1], [-1, -1],
            [-1, -1], [-1, -1], [-1, -1]]) == pg._persistence(X)[0]).all()
    assert pg.persistence_function(X).item() >= -2.7783148288726807 - 0.001
    pg.SGD(X, n_epochs=4, lr=0.4)


def test_PersistenceGradient_4d():
    '''check if the matrix input works properly'''
    X = torch.tensor([[1, 0., 1, 0.5], [0, 1., 0, 0.5],
                      [2, 2, 1, 0.5], [2, 1, 2, 0.5]])
    hom_dim = (0, 1)
    pg = PersistenceGradient(homology_dimensions=hom_dim,
                             zeta=0.1,
                             max_edge_length=3,
                             metric="precomputed",
                             collapse_edges=False)
    assert X.dtype == torch.float32
    assert pg.phi(X).shape[0] == 14
    assert (np.array([[0, 1], [-1, -1], [-1, -1],
                     [-1, -1]]) == pg._persistence(X)[0]).all()
    assert pg.persistence_function(X).item() >= 0.3467579483985901 + 0.001
    pg.SGD(X)


def test_PersistenceGradient_matrix():
    # simulate the weighted graph
    dist = torch.tensor([[0., 2, 3],
                        [2, 0., 2.2],
                        [3, 2.2, 0.]])

    pg = PersistenceGradient(homology_dimensions=(0, 1),
                             zeta=0.0,
                             collapse_edges=False,
                             metric="precomputed")
    assert all(pg.phi(dist) == torch.tensor([0., 0., 0., 2., 2.2, 3., 3.]))
    assert pg.persistence_function(dist).item() >= -4.2 - 0.0001
    fig, fig3d, loss_val = pg.SGD(dist, n_epochs=1,
                                  lr=0.002)
    assert (dist.grad == torch.tensor([[1., -1., 0.],
                                       [0., 1., -1.],
                                       [0., 0., 0.]])).all().item()


def test_PersistenceGradient_matrix_2():
    # simulate the weighted graph
    dist = torch.tensor([[0., 2., 10., 10.],
                         [2., 0., 2., 1],
                         [10., 2., 0., 1],
                         [10., 1, 1, 0.]])
    pg = PersistenceGradient(homology_dimensions=(0, 1),
                             zeta=0.0,
                             collapse_edges=False,
                             metric="precomputed")
    assert all(pg.phi(dist) == torch.tensor([0., 0., 0., 0., 1.,
                                             1., 2., 2., 2., 10.,
                                             10., 10., 10., 10.]))
    assert pg.persistence_function(dist).item() == -4.
    fig, fig3d, loss_val = pg.SGD(dist, n_epochs=1,
                                  lr=0.002)
