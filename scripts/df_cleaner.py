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

  