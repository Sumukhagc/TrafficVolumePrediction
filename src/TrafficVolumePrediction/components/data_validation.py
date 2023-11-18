from src.TrafficVolumePrediction.entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self,config:DataValidationConfig) -> None:
        self.config=config
        self.col=self.config.schema.keys()

    def validate_data(self):
        data=pd.read_csv(self.config.data)
        COLUMNS=list(data.columns)

        for c in COLUMNS:
            if(c not in self.col):
                with open(self.config.STATUS,'w') as f:
                    f.write("Validation Status : False")
            else:
                with open(self.config.STATUS,'w') as f:
                    f.write("Validation Status : True")
                           
