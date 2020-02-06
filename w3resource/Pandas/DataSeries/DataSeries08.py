import pandas

s = {'Name': ['Dani', 'Juancho', 'Carol'],  'Age': [30, 33, 31],
     'Position': ['Data Engineer', 'DevOps', 'Data Analyst']}
print(s)

df = pandas.DataFrame(s)
print(df)

gender = ['M','M', 'F']
df['Gender'] = gender
print(df)

names = df['Name']
print(names)