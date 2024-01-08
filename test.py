from datetime import datetime, timedelta

# Get the current date and time
current_datetime = datetime.now()

# Create a timedelta of 7 days
one_week = timedelta(days=7)

# Calculate the date and time one week from now
one_week_later = current_datetime + one_week

print("Current Date and Time:", current_datetime)
print("One Week Later:", one_week_later)
