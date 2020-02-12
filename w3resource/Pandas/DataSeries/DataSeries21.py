import pandas
import numpy as np
num_state = np.random.randint(10, size=10)
num_series = pandas.Series(num_state)

divisibles = []
for i in range(40):
    print(i)
    print(num_series[i])
    # if num_series[i] == 5:
    #    divisibles.append(i)

print(divisibles)