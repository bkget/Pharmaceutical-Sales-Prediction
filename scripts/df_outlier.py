import pandas as pd
import numpy as np
from log import get_logger

my_logger = get_logger("DfOutlier")
my_logger.debug("Loaded successfully!")


class DfOutlier:
  """
      Give an overview for a given data frame, 
      percentage of outliers in each column and 
      has methods for removeing or replacing outliers.
  """

  def __init__(self, df: pd.DataFrame) -> None:
    self.df = df

  def count_outliers(self, Q1, Q3, IQR):
    cut_off = IQR * 1.5
    temp_df = (self.df < (Q1 - cut_off)) | (self.df > (Q3 + cut_off))
    return [len(temp_df[temp_df[col] == True]) for col in temp_df]

  