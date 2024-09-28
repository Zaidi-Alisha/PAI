import re

text = "We have several dates in this text: 12/09/2023, 2023-09-12, and Sep 12, 2023. 
Another date is 01/01/2022"

# Regular expression to capture various date formats
date_pattern = r'(\d{2}/\d{2}/\d{4})|(\d{4}-\d{2}-\d{2})|([A-Za-z]{3} \d{2}, \d{4})'

dates = re.findall(date_pattern, text)

# Flatten the results
flat_dates = [date for group in dates for date in group if date]

print("Dates found:")
for date in flat_dates:
    print(date)


