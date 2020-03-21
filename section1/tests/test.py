import unittest
import pandas as pd
import os
from pandas.api.types import is_bool_dtype


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.root_path = os.path.dirname(os.path.abspath('../main.py'))
        self.output_path = os.path.join(self.root_path, "assets", "output")
        self.list_of_output_files = os.listdir(self.output_path)

    # What do i want to test? assertEqual(), assertTrue()/assertFalse() assertRaises()
    # Test whether the header contains above_100
    def test_header_contains_above_100_field(self):
        for file in self.list_of_output_files:
            file_path = os.path.join(self.output_path, file)
            data = pd.read_csv(file_path)
            is_above_100 = 'above_100' in data.columns
            self.assertTrue(is_above_100)

    # Test whether the header contains first name, last name
    def test_header_contains_first_name_and_last_name(self):
        for file in self.list_of_output_files:
            file_path = os.path.join(self.output_path, file)
            data = pd.read_csv(file_path)
            is_first_name = 'first_name' in data.columns
            is_last_name = 'last_name' in data.columns

            self.assertTrue(is_first_name)
            self.assertTrue(is_last_name)

    # Test whether the type of above_100 filed is boolean
    def test_above_100_datatype(self):
        for file in self.list_of_output_files:
            file_path = os.path.join(self.output_path, file)
            data = pd.read_csv(file_path)

            above_100_datatype = data['above_100']
            self.assertTrue(is_bool_dtype(above_100_datatype))

    # Test whether the output of the file is a csv
    def test_type_of_output_file_is_csv(self):
        for file in self.list_of_output_files:
            self.assertTrue(file.endswith('.csv'))


if __name__ == '__main__':
    unittest.main()
