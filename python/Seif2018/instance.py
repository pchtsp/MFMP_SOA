# /usr/bin/python3

import numpy as np
import package.auxiliar as aux
import package.data_input as di
import pandas as pd
import math


class Instance(object):
    """
    This represents the input data set used to solve.
    It doesn't include the solution.
    The methods help get useful information from the dataset.
    The data is stored in .input_data and it consists on a dictionary of dictionaries.
    The structure will vary in the future but right now is:
        * parameters: adimentional data
        * tasks: data related to tasks
        * resources: data related to resources
        * stations:
    """

    def __init__(self, input_data):
        self.input_data = input_data

