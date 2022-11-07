def is_leap_year(year):
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        return True
    return False


years = [1900, 1904, 1905, 2000, 2001, 2004, 2100]

for year in years:
    print(year, "leap year" if is_leap_year(year) else "not a leap year")
