import datetime

date = datetime.date(2025, 1, 2) # your own set time
today = datetime.date.today() # date today
print(date)
print(today)

time = datetime.time(12,30,0) # your own set time
now = datetime.datetime.now() # current date and time
print(time)
print(now)

now = now.strftime("Time: %H:%M:%S \nDate: %m-%d-%y") # "%" are format specifiers that can be found on datetime documentation online
print(now)

# seeing if the current date has passed 2030 Jan 1, 12:30:1
target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_date = datetime.datetime.now()

if target_datetime < current_date:
    print("Target date has already passed")
else:
    print("Target date has not passed")