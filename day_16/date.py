import datetime
from datetime import date, datetime

# Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(f"Day: {day}, Month: {month}, Year: {year}, Hour: {hour}, Minute: {minute}, Timestamp: {timestamp}")

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(now.strftime("%m/%d/%Y, %H:%M:%S"))

# Today is 5 December, 2019. Change this time string to time.
today = "5 December, 2019"
print("Today: ", datetime.strptime(today, "%d %B, %Y"))

# Calculate the time difference between now and new year.
new_year = datetime(year = 2026, month = 1, day = 1, hour = 0, minute = 0, second = 0)
print('Time left for new year:', new_year - datetime.now())

# Calculate the time difference between 1 January 1970 and now
epoch = datetime(1970, 1, 1)
print('Time difference between 1 January 1970 and now:', now - epoch)