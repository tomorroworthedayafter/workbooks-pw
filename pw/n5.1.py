from dateutil.parser import parse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
def read_data(input_file):
    input_data = np.loadtxt(input_file, delimiter = None)
    dates = pd.date_range('1950-01', periods=input_data.shape[0], freq='M')
    output = pd.Series(input_data[:, index], index=dates)
    return output


if __name__ == '__main__':
    input_file = r"C:\Users\san4o\AO.txt"
    timeseries = read_data(input_file)
    plt.figure()
    timeseries.plot()
    plt.show()
