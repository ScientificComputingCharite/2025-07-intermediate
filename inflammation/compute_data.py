"""Module containing mechanism for calculating standard deviation between datasets.
"""

import glob
import os
import numpy as np

from inflammation import models, views


def analyse_data(data_dir):
    """Calculates the standard deviation by day between datasets.

    Gets all the inflammation data from CSV files within a directory,
    works out the mean inflammation value for each day across all datasets,
    then plots the graphs of standard deviation of these means."""
    data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
    
    data = model.load_inflammation_data(data_file_paths)

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    graph_data = {
        'standard deviation by day': daily_standard_deviation,
    }
    views.visualize(graph_data)
