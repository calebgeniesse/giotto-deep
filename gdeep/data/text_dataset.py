import torch
from torch.utils.data import Dataset, DataLoader
from typing import Any, Tuple, Optional, Union
from .transforming_dataset import TransformingDataset


DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

Tensor = torch.Tensor


class TextDataset(TransformingDataset):
    """This class is the base class for the text-datasets.
    The source dataset for this class are expected to be
    dataset of the form ``(label, string)``.

    Args:
        dataset (torch Dataset):
            The source dataset for this class.
            It is expected to be a
            dataset of the form ``(label, string)``.
        transform (AbstractPreprocessing):
            the instance of the class of preprocessing.
            It inherits from ``AbstractPreprocessing``
        target_transform (AbstractPreprocessing):
            the instance of the class of preprocessing.
            It inherits from ``AbstractPreprocessing``

    Examples::

        from gdeep.data import TorchDataLoader
        from gdeep.data import TextDataset, PreprocessTextData, PreprocessTextLabel

        dl = TorchDataLoader(name="AG_NEWS", convert_to_map_dataset=True)
        dl_tr, dl_ts = dl.build_dataloaders()

        textds = TextDataset(dl_tr.dataset,
                             PreprocessTextData(),
                             PreprocessTextLabel())

    """

    def __init__(self, 
                 dataset: Dataset[Tuple[Any, Any]],
                 transform=None,
                 target_transform=None):
        super().__init__(transform=transform, target_transform=target_transform)
        self.dataset = dataset
        # initialise the preprocessing
        self.transform.fit_to_data(self.dataset)
        self.target_transform.fit_to_data(self.dataset)

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx : int) -> Tuple[Tensor, Tensor]:
        """The output of this method is a tuple of
        Two tensors. The first one is the tensor
        of tokenised words (i.e. a tensor of type ``torch.long``
        that contains the indices of the tokens within
        the vocabulary)"""
        text = self.dataset[idx][1]
        label = self.dataset[idx][0]
        text = self.transform(text)
        label = self.target_transform(label)
        if isinstance(label, Tensor) and isinstance(text, Tensor):
            sample = (text.to(torch.long), label.to(torch.long))
        else:
            sample = (text, torch.tensor(label, dtype=torch.long))
        return sample

class TextDatasetTranslation(TextDataset):
    """This class is the class for the text datasets
    dealing with translation tasks. The source data is expected
    to be of the form ``(string, string)`` containing the
    senteces to translate (left string translates into right string).

    Args:
        dataset (torch Dataset):
            The source dataset for this class.
            It is expected to be a
            dataset of the form ``(label, string)``.
        transform (AbstractPreprocessing):
            the instance of the class of preprocessing.
            It inherits from ``AbstractPreprocessing``
        target_transform (AbstractPreprocessing):
            the instance of the class of preprocessing.
            It inherits from ``AbstractPreprocessing``

    Returns:
        tensor, tensor:
            the first tensor has three dimensions, ``(BS, 2, MAX_LENGTH)``;
            this tensor represents the stacking of both the tokenisation
            of the source and target sentence.

    Examples::

        from gdeep.data import TorchDataLoader
        from gdeep.data import TextDatasetTranslation, PreprocessTextTranslation

        dl = TorchDataLoader(name="Multi30k", convert_to_map_dataset=True)
        dl_tr, dl_ts = dl.build_dataloaders()

        textds = TextDatasetTranslation(dl_tr.dataset,
            PreprocessTextTranslation(), None)

    """

    def __getitem__(self, idx: int) -> Tuple[Tensor, Tensor]:
        text = self.dataset[idx]
        if self.transform:
            text = self.transform(text)
        # unique tensor containing both tensors of the target and source
        sample = torch.stack([text[0].to(torch.long), text[1].to(torch.long)])
        y = text[1].to(torch.long).clone().detach()

        return (sample, y)


class TextDatasetQA(TextDataset):
    """This class is the class for the text datasets
    dealing with Q&A tasks. The source data is expected
    to be of the form ``(string, string, list[string], list[int])`` containing the
    sentences ``(context, question, [answer(s)],
    [initial position (in characters) of the answer(s)]))``.

    Args:
        dataset (torch Dataset):
            The source dataset for this class.
            It is expected to be a
            dataset of the form ``(label, string)``.
        transform (AbstractPreprocessing):
            the instance of the class of preprocessing.
            It inherits from ``AbstractPreprocessing``
        target_transform (AbstractPreprocessing):
            the instance of the class of preprocessing.
            It inherits from ``AbstractPreprocessing``

    Returns:
        tensor, tensor:
            the first tensor has three dimensions, ``(BS, 2, MAX_LENGTH)``;
            this tensor represents the stacking of both the tokenisation
            of the context and question sentence.
            The second tensor is just the batch of pairs of start and
            end positions of the answers

    Examples::

        from gdeep.data import TorchDataLoader
        from gdeep.data import  TextDatasetQA, PreprocessTextQA, PreprocessTextQATarget

        dl = TorchDataLoader(name="SQuAD2", convert_to_map_dataset=True)
        dl_tr, dl_ts = dl.build_dataloaders()

        textds = TextDatasetQA(dl_tr_str.dataset,
                               PreprocessTextQA(),
                               PreprocessTextQATarget())

    """

    def __getitem__(self, idx:int) -> Tuple[Tensor, Tensor]:

        context, question = self.transform(self.dataset[idx])
        pos_init, pos_end = self.target_transform(self.dataset[idx])
        #sample = [(context.to(torch.long), question.to(torch.long)), (pos, answer.to(torch.long))]
        sample = [torch.stack((context, question)).to(torch.long),
                  torch.stack((pos_init, pos_end)).to(torch.long)]
        return sample

