import pandas

d = {'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]}
df = pandas.DataFrame(d)
df = df.rename(columns={'X': 'Column1', 'Y': 'Column2', 'Z': 'Column3'})

print(df)