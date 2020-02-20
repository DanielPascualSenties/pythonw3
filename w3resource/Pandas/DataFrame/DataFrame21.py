import pandas
import numpy as np

exam_data = [{'name': 'Anastasia', 'score': 12.5}, {'name': 'Dima', 'score': 9}, {'name': 'Katherine', 'score': 16.5}]

df = pandas.DataFrame(exam_data)

for i, row in df.iterrows():
    print(row['name'], row['score'])
