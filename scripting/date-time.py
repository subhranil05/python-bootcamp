import datetime


tmp_date = datetime.date(2023, 11, 8)
today = datetime.date.today()

today_delta = datetime.timedelta(days=5)   # 5 days after from today

my_bday = datetime.date(2023, 11, 1)

print(tmp_date)
print(today)

print(today.weekday())
print(today.isoweekday())

print(today + today_delta)

print(f"{my_bday - today} Days remains to by birthday")


tmp_time = datetime.time()

print(tmp_time)