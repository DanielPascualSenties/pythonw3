import pandas
import numpy as np
num_state = np.random.randint(10, size=40)
num_series = pandas.Series(num_state)

histogram = num_series.value_counts()


#TODO