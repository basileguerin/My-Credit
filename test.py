import unittest
from functions import get_data, standardize_labelize, train_model, test_model

class TestModel(unittest.TestCase):
    train_path = './test.csv'
    test_path = './train.csv'

    def test_data(self):
        get_data(self.train_path)

    def test_standard(self):
        df = get_data(self.train_path)
        standardize_labelize(df)

    def test_model(self):
        model, scalers, encoders = train_model(self.train_path)
        test_model(self.test_path, model, scalers, encoders)