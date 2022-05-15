from typing import Any, Callable, Iterable, TypeVar

from torch.utils.data import Dataset

from .abstract_preprocessing import AbstractPreprocessing
from .transforming_dataset import TransformingDataset

T = TypeVar('T')

class PreprocessingPipeline:
    """ Pipeline to fit non-fitted preprocessors to a dataset in a sequential manner.
    The fitted preprocessing transform can be attached to a dataset using
    the ´attach_transform_to_dataset´ method.
    The intended use case is to fit the preprocessors to the training dataset and
    then attach the fitted transform to the training, validation and test datasets.
    
    The transform is only applied to the data and not the labels.
    
    Examples::

        from gdeep.data import PreprocessingPipeline, Normalize, \
            PreprocessImageClassification

        image_dataset = DatasetImageClassificationFromFiles(
            os.path.join(file_path, "img_data"),
            os.path.join(file_path, "img_data", "labels.csv"))
        
        preprocessing_pipeline = PreprocessingPipeline((PreprocessImageClassification((30, 30)),
                                                        Normalize()))
        preprocessing_pipeline.fit_to_dataset(image_dataset)  # this fill not change the image_dataset
        preprocessed_dataset = preprocessing_pipeline.attach_transform_to_dataset(image_dataset)
    """
    
    transform = Callable[[T], Any]
    def __init__(self, preprocessors: Iterable[AbstractPreprocessing[Any, Any]]) -> None:
        self.preprocessors = preprocessors
    
    def attach_transform_to_dataset(self, dataset: Dataset[T]) -> TransformingDataset[T, Any]:
        return TransformingDataset(dataset, self.transform)

    def fit_to_dataset(self, dataset: Dataset[Any]) -> None:
        def id_transform(x: Any) -> Any:
            return x
        self.transform = id_transform
        transformed_dataset = TransformingDataset(dataset, self.transform)
        for preprocessor in self.preprocessors:
            preprocessor.fit_to_dataset(transformed_dataset)
            transformed_dataset.append_transform(preprocessor)
        self.transform = transformed_dataset.transform