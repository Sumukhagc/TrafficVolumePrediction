from src.TrafficVolumePrediction.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from src.TrafficVolumePrediction.utils.common import read_yaml,create_directories
from src.TrafficVolumePrediction.entity import DataIngestionConfig
class ConfigurationManager:
    def __init__(self) -> None:
        self.config=read_yaml(CONFIG_FILE_PATH)
        self.params=read_yaml(PARAMS_FILE_PATH)
        create_directories([self.config['artifacts_root']])

    def get_data_ingestion_config(self):
        config=self.config['data_ingestion']
        create_directories([config['root_dir']])
        return DataIngestionConfig(config['root_dir'],config['source_url'],config['local_dir'],config['unzip_dir'])