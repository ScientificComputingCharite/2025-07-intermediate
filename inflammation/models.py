"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np
import json
from glob import glob
import os


def load_csv(filename):  
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')



class DataLoader:
    def __init__(self, fname):
        self.fname = fname
        self._data = None

    def get_data(self):
        raise NotImplementedError

    @property
    def data(self):
        if self._data is None:
            self._data = self.get_data()
        return self._data

    @property
    def daily_mean(self):
        return np.mean(self.data, axis=0)

    @property
    def daily_min(self):
        return np.min(self.data, axis=0)
    
    @property
    def daily_max(self):
        return np.mean(self.data, axis=0)

    @property
    def view_data(self):
        return {
            "average": self.daily_mean,
            "max": self.daily_max,
            "min": self.daily_min,
        }

class CSVLoader(DataLoader):
    def get_data(self):
        return np.loadtxt(fname=self.fname, delimiter=',')

class JSONLoader(DataLoader):
    def get_data(self):
        with open(self.fname, 'r', encoding='utf-8') as file:
            data_as_json = json.load(file)
        return [np.array(entry['observations']) for entry in data_as_json]

