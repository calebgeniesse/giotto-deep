import torch
from abc import ABC, abstractmethod
import warnings
import os
import json
import jsonpickle

Tensor = torch.Tensor

if torch.cuda.is_available():
    DEVICE = torch.device("cuda")
else:
    DEVICE = torch.device("cpu")


class AbstractPreprocessing(ABC):
    """The abstract class to define the interface of preprocessing
    """
    @abstractmethod
    def transform(self, *args, **kwargs):
        """This method deals with datum-wise transformations. This
        method is called in the Datasets to transform the output
        of ``__getitem__``"""
        pass

    @abstractmethod
    def fit_to_data(self, *args, **kwargs):
        """This method deals with getting dataset-level information.
        """
        pass

    def save_pretrained(self, path):
        with open(os.path.join(path, self.__class__.__name__ + ".json"), "w") as outfile:
            whole_class = jsonpickle.encode(self)
            json.dump(whole_class, outfile)

    def load_pretrained(self, path):
        try:
            with open(os.path.join(path,self.__class__.__name__ + ".json"), "r") as infile:
                whole_class = json.load(infile)
                self = jsonpickle.decode(whole_class)
        except FileNotFoundError:
            warnings.warn("The transformation file does not exist; attempting to run"
                          " the transformation anyway...")
