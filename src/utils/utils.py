import pandas as pd

class Utility:
    
    @staticmethod
    def verify_individual_counts(df: pd.DataFrame, v: str=None, variables: list[str]=None) -> None:
        """
        This function verifies that there are no duplicates in the rows 
        like UID and customer_id where there should not be a duplicate.
        Output is used for visual verification.
        """
        if variables:
            for v in variables:
                count = df[v].value_counts().count()
                filled = df[v].value_counts().count() == 10000
                print(f"{v} has {count} rows. All values filled = {filled}")
        elif v:
            count = df[v].value_counts().count()
            filled = df[v].value_counts().count() == 10000
            print(f"{v} has {count} rows. All values filled = {filled}")
        else:
            print("No variable specified for analysis.")
    
    @staticmethod
    def verify_value_counts(df: pd.DataFrame, v: str=None, variables: list[str]=None) -> None:
        """
        This function will check the counts of each value for the variabels
        that are passed to it.
        """
        if variables:
            for v in variables:
                results = df[v].value_counts()
                print (f" Now analyzing variable: {v} \n value_counts() returned:{results} \n \n")
        elif v:
            results = df[v].value_counts()
            print (f" Now analyzing variable: {v} \n value_counts() returned:{results} \n \n")
        else:
            print("No variable specified for analysis.")
    @staticmethod
    def describe_variable(df: pd.DataFrame, v: str=None, variables: list[str]=None) -> None:
        """
        This function will print the following values for each variable passed
        
        Variables:
            - count    
            - mean       
            - std        
            - min        
            - 25%        
            - 50%        
            - 75%         
            - max        
            - Name 
            - dtype
        """
        if variables:
            for v in variables:
                results = df[v].describe()
                print(f"Now analyzing variable: {v} \n describe() returned: {results} \n \n")
        elif v:
            results = df[v].describe()
            print(f"Now analyzing variable: {v} \n describe() returned: {results} \n \n")
        else:
            print("No variable specified for analysis.")

    @staticmethod
    def display_unique_values(df: pd.DataFrame, v: str=None, variables: list[str]=None) -> None:
        """
        This function displays all unique values for a variable
        """
        if variables:
            for v in variables:
                values = df[v].unique() 
                print(f"{v} has the following values: \n{values}")
        elif v:
            values = df[v].unique() 
            print(f"{v} has the following values: \n{values}")
        else:
            print("No variable specified for analysis.")

    @staticmethod
    def check_zip(df: pd.DataFrame, v: str) -> None:
        df['Zip'] = df['Zip'].astype(str)
        df = df[df['Zip'].str.len() != 5]
        print(f"The following rows only have 4 digits:\n{df['Zip']}")
        
    @staticmethod 
    def fix_zip(df: pd.DataFrame, v: str) -> pd.DataFrame:
        df['Zip'] = df['Zip'].astype(str)
        df['zip_code'] = df['zip_code'].str.zfill(5)
        return df
        
    @staticmethod 
    def insert_space() -> str:
        return " \n\n\n\n\n ********************************************* \n ********************************************* \n "
