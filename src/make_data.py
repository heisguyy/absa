from importlib.resources import path
import kaggle

def create_data(name_of_dataset: str, storage_path: str) -> None:
    """Sources data from kaggle and stores it into a specified directory.

    Args:
        name_of_dataset (str): Name of dataset on kaggle.
        storage_path (str): relative system path to the storage directory.
    """
    kaggle.api.authenticate()

    kaggle.api.dataset_download_files(dataset=name_of_dataset,path=storage_path,unzip=True)


if __name__ == "__main__":
    name = "kandhalkhandeka/data-for-aspect-based-sentimental-analysis"
    store_path = "../data/raw/"
    create_data(name_of_dataset=name,storage_path=store_path)