from src.TrafficVolumePrediction.components.data_validation import DataValidation
from src.TrafficVolumePrediction.config.configuration import ConfigurationManager
from src.TrafficVolumePrediction.entity import DataValidationConfig
class DataValidationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation_config=DataValidation(data_validation_config)
        data_validation_config.validate_data()
