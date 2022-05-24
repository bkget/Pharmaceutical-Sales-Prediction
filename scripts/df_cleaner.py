import numpy as np
import pandas as pd
from log import get_logger

my_logger = get_logger("DfCleaner")
my_logger.debug("Loaded successfully!")


class DfCleaner():
  """
      Has functions for cleans pandas data frame by removing duplicates, 
      droping columns or rows and more.
  """

  def __init__(self):
    pass

  def fixLabel(self, label: list) -> list:
    """convert list of labels to lowercase separated by underscore
    Args:
        label (list): list of labels 
    Returns:
        list: list of labels in lower case, separated by underscore
    """
    label = label.strip()
    label = label.replace(' ', '_').replace('.', '').replace('/', '_')
    return label.lower()

  def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
    """drop duplicate rows
    Args:
        df (pd.DataFrame): pandas data frame
    Returns:
        pd.DataFrame: pandas data frame
    """
    df.drop_duplicates(inplace=True)
    return df

  def drop_columns(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """ drop selected columns from data frame
    Args:
        df (pd.DataFrame):  pandas data frame
        columns (list): list of column labels
    Returns:
        pd.DataFrame: pandas data frame columns dropped
    """
    for col in columns:
      df.drop(col, axis=1, inplace=True)
    return df

  def drop_rows(self, df: pd.DataFrame, column: str, row_value: str) -> pd.DataFrame:
    """drop rows in selected column based on condition given
    Args:
        df (pd.DataFrame): pandas data frame
        column (str): column label
        row_value (str): condition to check againest
    Returns:
        pd.DataFrame: pandas data frame with rows dropped
    """
    df = df.drop(df[df[column] != row_value].index)
    return df

  