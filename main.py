import pandas as pd
from src.cleaning import IdentifyData
from src.utils import Utility

class Config:
    def __init__(self, path_to_csv: str):
        self.df = pd.read_csv(path_to_csv)
        self.util = Utility()
        self.id = id
        

def main(config: Config) -> None:
    # Break it down into data loading, data cleaning, and data visualization.
    pass



if __name__ == "__main__":
    path_to_csv = 'd206/medical_data.csv'
    config = Config(path_to_csv)
    main(config)