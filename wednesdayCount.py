from datetime import datetime, timedelta

# Define the date range
start_date = datetime(1980, 4, 16)
end_date = datetime(2009, 2, 11)

# Initialize a counter for Wednesdays
wednesday_count = 0

# Iterate through the date range
current_date = start_date
while current_date < end_date:
    if current_date.weekday() == 2:  # 2 represents Wednesday
        wednesday_count += 1
    current_date += timedelta(days=1)

# Output the total number of Wednesdays
print(wednesday_count)
