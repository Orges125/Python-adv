import datetime

current_datime = datetime.datetime.now()

print("Year:",current_datime.year)
print("Month:",current_datime.month)
print("Day:",current_datime.day)
print("Hour:",current_datime.hour)
print("Minute:",current_datime.minute)

current_date = datetime.datetime.now().date()
print(current_date)

current_time = datetime.datetime.now().time()
print(current_time)