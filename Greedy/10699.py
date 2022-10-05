import datetime
x = datetime.datetime.now()
month = x.month
if month < 10:
    month = "0"+str(month)
day = x.day
if day < 10:
    day = "0" + str(day)
print(f"{x.year}-{month}-{day}")
