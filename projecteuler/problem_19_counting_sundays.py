from datetime import date

SUNDAY = 6

print(sum(date(year, month, 1).weekday() == SUNDAY for month in range(1, 13) for year in range(1901, 2001)))
# Expected: 171
