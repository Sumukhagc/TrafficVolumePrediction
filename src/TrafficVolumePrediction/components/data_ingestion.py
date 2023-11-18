from src.TrafficVolumePrediction.entity import DataIngestionConfig
import os
from src.TrafficVolumePrediction.logging import logger
from urllib import request
import zipfile 
class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config=config

    def download_data(self):
        if(not os.path.exists(self.config.local_dir)):
            filename,headers=request.urlretrieve(self.config.source_url,self.config.local_dir)
            logger.info("Downloaded the data successfully")
        else:
            logger.info("Data already exists")

    def unzip_data(self):
        unzip_dir_path=self.config.root_dir
        os.makedirs(unzip_dir_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_dir,'r') as zip_ref:
            zip_ref.extractall(unzip_dir_path)
