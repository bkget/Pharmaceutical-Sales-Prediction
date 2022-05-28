import os
import sys
import unittest
from numpy import number
import pandas as pd
import pandas.api.types as ptypes
from pandas.api import types

sys.path.append(os.path.abspath(os.path.join('../scripts')))
from df_cleaner import DfCleaner 

class TestDfCleaner(unittest.TestCase):

    def setUp(self) -> pd.DataFrame:
        self.cleaner = DfCleaner()

    def test_convert_to_datetime(self):
        df = pd.DataFrame({'col1': ["2018-01-05", "2018-01-06"]})
        df = self.cleaner.convert_to_datetime(df, ['col1'])
        self.assertTrue(type(df['col1'].dtype == ptypes.DatetimeTZDtype))

    def test_convert_to_integer(self):

        df = pd.DataFrame({'col1': ["1", "2"]})
        df = self.cleaner.convert_to_numbers(df, ['col1'])
        self.assertTrue(types.is_int64_dtype(df['col1']))

if __name__ == '__main__':
    unittest.main()