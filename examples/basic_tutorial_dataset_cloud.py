# %% 
from IPython import get_ipython  # type: ignore
get_ipython().magic('load_ext autoreload')
get_ipython().magic('autoreload 2')

# %%
import torch
from gdeep.data import DlBuilderFromDataCloud, DatasetCloud
from os import remove
from os.path import join


# %%

def create_and_upload_dataset():
    # Generate a dataset
    # You do not have to do that if you already have a pickled dataset
    size_dataset = 100
    input_dim = 5
    num_labels = 2
    data = torch.rand(size_dataset, input_dim)
    labels = torch.randint(0, num_labels, (size_dataset,)).long()

    # pickle data and labels
    data_filename = 'tmp_data.pt'
    labels_filename = 'tmp_labels.pt'
    torch.save(data, data_filename)
    torch.save(labels, labels_filename)

    ## Upload dataset to Cloud
    dataset_name = "SmallDataset"
    dataset_cloud = DatasetCloud(dataset_name)

    # Specify the metadata of the dataset
    dataset_cloud.add_metadata(
        name=dataset_name,
        size_dataset=size_dataset,
        num_labels=num_labels,
        data_type="tabular",
        data_format="pytorch_tensor"
    )

    # upload dataset to Cloud
    dataset_cloud.upload(data_filename, labels_filename)

    # remove the labels and data files
    # Warning: Only do this if you do want the local dataset to be deleted!
    remove(data_filename)
    remove(labels_filename)
    
create_and_upload_dataset()

# %%
# Create dataloaders from data cloud
# If you don't know what datasets exist in the cloud, just use an empty
# ´dataset_name´ and then the error message will display all available datasets 
dataset_name = "AdversarialAttackDataset"
download_directory = join("data", "DatasetCloud")

dl_cloud_builder = DlBuilderFromDataCloud(dataset_name,
                                   download_directory)

# You can display the metadata of the dataset
print(dl_cloud_builder.get_metadata())

# create the dataset from the downloaded dataset
train_dataloader, val_dataloader, test_dataloader = dl_cloud_builder.build_dataloaders(batch_size=10)
# %%
# Check if the dataloader have the correct shape
x, y = next(iter(train_dataloader))
y.shape
# %%
## Upload dataset to Cloud
dataset_name = "CurvatureDataset"
dataset_cloud = DatasetCloud(dataset_name)
data_filename = "data\diagrams_5000_1000_0_1.npy"
labels_filename = "data\curvatures_5000_1000_0_1.npy"

# Specify the metadata of the dataset
dataset_cloud.add_metadata(
    name=dataset_name,
    size_dataset=5_000,
    task_type="regression",
    num_labels=None,
    data_type="tabular",
    data_format="numpy_array",
    input_size=(1300, 4),
    comment="Curvature dataset as described in the persformer paper"
)

# upload dataset to Cloud
dataset_cloud.upload(data_filename, labels_filename)
# %%
import pickle
with open("data\AdversarialAttackDataset\labels_subsample.pkl", 'rb') as f:
    labels = torch.tensor(pickle.load(f), dtype = torch.long)[:, 1]
with open("data\AdversarialAttackDataset\diagrams_MNIST_subsample_500.pkl", 'rb') as f:
    data = torch.tensor(pickle.load(f), dtype = torch.float32)

# pickle data and labels
data_filename = 'tmp_data.pt'
labels_filename = 'tmp_labels.pt'
torch.save(data, data_filename)
torch.save(labels, labels_filename)

## Upload dataset to Cloud
dataset_name = "AdversarialAttackDataset"
dataset_cloud = DatasetCloud(dataset_name)

# Specify the metadata of the dataset
dataset_cloud.add_metadata(
    name=dataset_name,
    size_dataset=12_000,
    num_labels=2,
    task_type="classification",
    data_type="tabular",
    data_format="pytorch_tensor",
    input_size=(500, 2),
    comment="Adversarial Attack dataset for more information ask Nicolas."
)

# upload dataset to Cloud
dataset_cloud.upload(data_filename, labels_filename)
# %%
from gdeep.topology_layers import load_data_as_tensor
# %%
