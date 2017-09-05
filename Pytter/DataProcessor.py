import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class DataProcessor(object):
    """TODO: Add object descriptor"""
    def __init__(self, file_path=None):
        self.pddata = None
        self.npdata = None
        self.data = None
        self.parameter_list = None
        if file_path == None:
            self.file_path = file_path
        else:
            self.load_csv(file_path)

    def __str__(self):
        if(self.data == None):
            return "This data processor is empty."
        else:
            return str(self.pddata) + "\n\tpddata\n" #+ str(self.npdata) + "\n\tnpdata\n" + str(self.data) + "\n\tdata\n"

    def __len__(self):
        if self.parameter_list == None:
            return 0
        else:
            return len(self.parameter(list))

    def update_data(self):
        self.npdata = self.pddata.as_matrix()
        self.data = self.npdata.tolist()
        self.parameter_list = list(self.pddata.columns.values)

    def load_csv(self, file_path):
        self.pddata = pd.read_csv(file_path)
        self.file_path = file_path
        self.update_data()

    def store(self, file_path):
        self.pddata.to_csv(path=file_path, header=True)

    def get_parameter_list(self):
        return self.parameter_list

    def add_column(self, data, label=None):
        self.pddata = pd.concat([self.pddata, pd.Series(data, name=label)], axis=1)
        self.update_data()

    def add_row(self, new_row_array):
        print(new_row_array, "new_row_array")
        print(self.pddata, "data before")
        self.pddata.append(pd.DataFrame([new_row_array]))
        print(self.pddata, "data after")
        self.update_data()

    def get_column_np(self, header=None, index=None):
        assert header != None or index != None, "Please supply either a header parameter or index"
        if index != None:
            assert type(index) == type(3), "index is not an integer"
            assert index >= 0, "index is less than 0"
            assert index < len(self.parameter_list), "index is greater than parameter size"
            return self.npdata[:,index]
        if header != None:
            assert type(header) == type(""), "header must be a string"
            self.assert_listed(header)
            index = self.parameter_list.index(header)
            return self.npdata[:,index]

       
    def plot_2d(self, x, y):
        assert type(x) == type("3") or type(x) == type(3), "Please supply an integer or header string matching a parameter within the dataset for your x-axis"
        assert type(y) == type("3") or type(y) == type(3), "Please supply an integer or header string matching a parameter within the dataset for your y-axis"
        if type(x) == type("3"):
            self.assert_listed(x)
            x = self.parameter_list.index(x)
        if type(y) == type("3"):
            self.assert_listed(y)
            y = self.parameter_list.index(y)

        plt.plot(self.get_column_np(index=x), self.get_column_np(index=y))
        plt.show()

    def assert_listed(self, parameter, alias=None):
        if alias == None:
            assert parameter in self.parameter_list, "It seems " + parameter + " is not listed as a parameter in the data file provided.  Please supply an alias."
        else:
            assert alias in self.parameter_list, "Given alias, \"" + alias + "\", for " + parameter + " not found within parameter list."