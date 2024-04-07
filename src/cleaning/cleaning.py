import seaborn # For Boxplots
import statistics # for mean, median, and mode
import pandas as pd
import missingno as msno # For data cleaning specifically
import scipy.stats as stats # For calculating z-scores
import matplotlib.pyplot as plt # for histograms/visuals
from sklearn.decomposition import PCA # For PCA
from abc import ABC, abstractmethod
from src.utils import Utility

class Identify(ABC):
    @abstractmethod
    def identify(self) -> None:
        pass
        
class Clean(ABC):      
    @abstractmethod
    def clean(self) -> None:
        pass

class IdentifyData(Identify):
    def __init__(self, path_to_df: str=None, df: pd.DataFrame=None) -> None:
        if path_to_df:
            self.df = pd.read_csv(path_to_df) # Import the csv file to a dataframe
        elif df:
            self.df = df
        else:
            print(" Please provide a pd.DataFrame of a Path when instantiating this class.")
            return
        self.utility = Utility()
        pd.set_option("display.max_columns", None) # View all columns
        self.has_null = [] # List to store columns with null values
        self.boolean_columns = []  # List to store columns with boolean values


    def identify(self):
        self.find_variables_with_null()
        self.display_info()
        

    def clean(self):
        pass

    def display_info(self) -> None:
        """
        Display information about the DataFrame, duplicated value counts, and null value distribution chart.
        """
        try:
            # Display DataFrame info
            print("DataFrame Info:")
            self.df.info()
            
            # Display duplicated value counts
            print("\n\n\n\n Analysis of the duplicated value counts:")
            print(self.df.duplicated().value_counts())
            
            # Display null value distribution chart
            print("\n\n\n\n Chart depicting the null value distribution:")
            msno.matrix(self.df, labels=True)
            plt.show()  # Display the chart

            # Display the boolean columns
            self.detect_boolean_columns()
            print("\n\n\nThe following columns have boolean values:")
            for v in self.boolean_columns:
                print(v)
            print("\n\n\n\n")

            # Display histograms for data with missing data
            self.plot_histogram()
            
        except Exception as e:
            print(f"The following exception occurred: {e}")
        
    def find_variables_with_null(self) -> None:
        """
        This function checks all of the null counts for the variables, 
        and if it does have null values, it adds it to the list called 
        null_counts:
            - variable
        """
        df = self.df
        null_counts = df.isnull().sum()
        for variable, null_count in null_counts.items():
            # If null_count is greater than 0, add the variable to has_null
            if null_count > 0:
                self.has_null.append(variable)
                
    def detect_boolean_columns(self) -> None:
        """
        Detects columns with boolean values and returns a list of column names.
        """
        for col in self.df.columns:
            if self.is_boolean_column(col):
                self.boolean_columns.append(col)

    def is_boolean_column(self, col: str) -> bool:
        """
        Checks if a column contains boolean values and returns True if it does, False otherwise.
        """
        unique_values = self.df[col].dropna().unique()
        if all(val in {"yes", "no"} for val in unique_values) or \
           all(val in {"Yes", "No"} for val in unique_values) or \
           all(val in {0, 1} for val in unique_values):
            return True
        return False

    def plot_histogram(self) -> None:
        """
        For all columns with null values, plot histograms.
        """
        try:
            histograms = []  # List to store histograms
            for v in self.has_null:
                if v in self.boolean_columns:
                    print(f"Skipping histogram for boolean column: {v}, ***MISSING VALUES DETECTED***")
                    continue

                hist, bins, _ = plt.hist(self.df[v].dropna(), bins=20)
                plt.close()
                histograms.append((v, hist, bins))

            for hist_data in histograms:
                v, hist, bins = hist_data
                plt.bar(bins[:-1], hist, width=(bins[1]-bins[0]), align='edge', label=v)
                plt.legend()
                plt.xlabel("Values")
                plt.ylabel("Frequency")
                plt.title("Histograms for Variables with Null Values")
                plt.show()

        except Exception as e:
            print(f"The following exception occurred: {e}")
            
    def determine_category_assignment(self, variables: list[str]) -> None:
        space = self.utility.insert_space()
        for v in variables:
            col_dtype = self.df[v].dtype
            if col_dtype == 'object':
                print(f"{space} \n Now Processing {v} dtype: {col_dtype}")
                self.utility.verify_value_counts(self.df, v)
            elif col_dtype in ['int64', 'float64']:
                print(f"{space} \n Now Processing {v} dtype: {col_dtype}")
                self.utility.describe_variable(self.df, v)
            else:
                print(f"{space} \n Now Processing {v} dtype: {col_dtype}")

