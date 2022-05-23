import json
import os
import shutil
import warnings
from abc import ABC, abstractmethod
from os.path import join
from collections.abc import Iterable
from typing import Any, Callable, Dict, Optional, Tuple, \
    TypeVar, Union, List

import numpy as np
import pandas as pd
import torch
from PIL import Image, UnidentifiedImageError
from sympy import false
from torch.utils.data import DataLoader, Dataset
from torchvision.transforms import Resize, ToTensor
from tqdm import tqdm

from .build_datasets import get_dataset
from .dataset_cloud import DatasetCloud
from ..transforming_dataset import TransformingDataset


Tensor = torch.Tensor
T = TypeVar('T')

class AbstractDataLoaderBuilder(ABC):
    """The abstractr class to interface the
    Giotto dataloaders"""
    @abstractmethod
    def build(self):
        pass


class DataLoaderBuilder(AbstractDataLoaderBuilder):
    """This class builds, out of a tuple of datasets, the
    corresponding dataloaders. Note that this class would
    use the same parameters for all the datasets

    Args:
        tuple_of_datasets :
            the tuple eith the traing, validation and test
            datasets. Also one or two elemennts are acceptable:
            they will be considered as training first and
            validation afterwards.
    """
    def __init__(self, tuple_of_datasets: List[Dataset[Any]]) -> None:
        self.tuple_of_datasets = tuple_of_datasets
        assert len(tuple_of_datasets) <= 3, "Too many Dataset inserted: maximum 3."

    def build(self,
              tuple_of_kwargs:Optional[List[Dict[str, Any]]]=None
              ) -> List[DataLoader[Any]]:
        """This method accepts the arguments of the torch
        Dataloader and applies them when creating the
        tuple

        Args:
            tuple_of_kwargs:
                List of dictionaries, each one being the
                kwargs for the corresponding DataLoader
        """
        if tuple_of_kwargs:
            assert len(tuple_of_kwargs) == len(self.tuple_of_datasets), \
                "Cannot match the dataloaders and the parameters. "
            out: List = []
            for dataset, kwargs in zip(self.tuple_of_datasets, tuple_of_kwargs):
                out.append(DataLoader(dataset, **kwargs))
            out += [None] * (3 - len(out))
            return out
        else:
            out: List = []
            for i, dataset in enumerate(self.tuple_of_datasets):
                out.append(DataLoader(dataset))
            out += [None] * (3 - len(out))
            return out
