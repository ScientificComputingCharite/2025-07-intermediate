#!/usr/bin/env python3
"""
Software for managing and analysing patients' inflammation data
in our imaginary hospital.
"""

import argparse
import os
from pathlib import Path

from inflammation import models, views
from inflammation.compute_data import analyse_data


def load_data(fname: Path):
    if fname.is_dir():
        for f in fname.glob("*"):
            for d in load_data(f):
                yield d
    else:
        if fname.suffix == ".csv":
            yield models.CSVLoader(fname)
        elif fname.suffix == ".json":
            yield models.JSONLoader(fname)
        else:
            print(f"Warning, unknown file {fname}")

def main(args):
    """The MVC Controller of the patient inflammation data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    
    data = []
    for filename in args.infiles:
        for d in load_data(filename):
            data.append(d)

    for d in data:
        print(type(d))
        views.visualize(d.view_data)
        
    
    #if args.load_directory:
    #    data = models.CSVLoader(os.path.dirname(infiles[0]))
    #else:
    #    data = []
    #    for filename in infiles:
    #        data.append(models.load_csv(filename))

        
        

    #if args.full_data_analysis:
    #    graph_data = analyse_data(data)
    #    views.visualize(graph_data)
    #else:
    #    for d in data:
    #        view_data = {
    #            'average': models.daily_mean(inflammation_data),
    #            'max': models.daily_max(inflammation_data),
    #            'min': models.daily_min(inflammation_data)
    #        }
    #        views.visualize(view_data)

        view_data = {'average': models.daily_mean(inflammation_data), 'max': models.daily_max(inflammation_data), 'min': models.daily_min(inflammation_data)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic patient inflammation data management system')

    parser.add_argument(
        'infiles',
        nargs='+',
        type=Path,
        help='Input CSV(s) containing inflammation series for each patient')

    parser.add_argument(
        "-d", "--load-directory", action="store_true", default=False,
        help="load all files from directory")

    parser.add_argument(
        '--full-data-analysis',
        action='store_true',
        dest='full_data_analysis')

    args = parser.parse_args()

    main(args)
