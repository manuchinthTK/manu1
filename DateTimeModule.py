from datetime  import datetime

#dt = datetime(2024, 9,25, 9,6,5)

#now =datetime.now()
#print(now.time())

from datetime  import date

#d = date(2024, 9, 25)
#print(d)

#today = date.today()
#print(today)

from datetime import time

#t = time(1, 2, 3)
#print(t)
#print(t.hour)

from datetime import timedelta

#delta = timedelta(days=5, hours=3, seconds=30)

#print("Time delta:", delta)

#today = date.today()

#print("Before Date:", today)

#future_date = today + timedelta(days=-7)

#print("After Date:", future_date)


from datetime import time

date1 = datetime(2023, 9, 22, 10, 10)
date2 = datetime(2024, 9, 22, 10, 10)

print(date2-date1)


from calendar import isleap

print(isleap(2024))