from src.TrafficVolumePrediction.components.data_ingestion import DataIngestion
from src.TrafficVolumePrediction.config.configuration import ConfigurationManager
from src.TrafficVolumePrediction.entity import DataIngestionConfig
class DataIngestionPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        print("x")
        config=ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.unzip_data()
