import datetime
from datetime import timedelta
dateWedding = datetime.datetime(2019, 11, 2, 12, 30, 00)
dateNow = datetime.datetime.now()
dif = dateNow - dateWedding
print(dif)
