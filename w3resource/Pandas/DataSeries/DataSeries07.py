import pandas

s = pandas.Series([51, 27, "galleta", 48.1231, 15])
print(s)

ns = pandas.to_numeric(s,errors="coerce")
print(ns)
