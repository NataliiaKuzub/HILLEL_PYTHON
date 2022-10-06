birth_month = int(input("Please, enter your month of birth (as a number from 1 to 12): "))
birth_date = int(input("Please, enter your date of birth: "))
if birth_month == 1 and 20 <= birth_date <= 31 or birth_month == 2 and 1 <= birth_date <= 18:
    print("You are Aquarius!")
elif birth_month == 2 and 19 <= birth_date <= 29 or birth_month == 3 and 1 <= birth_date <= 20:
    print("You are Pisces!")
elif birth_month == 3 and 21 <= birth_date <= 31 or birth_month == 4 and 1 <= birth_date <= 19:
    print("You are Aries!")
elif birth_month == 4 and 20 <= birth_date <= 30 or birth_month == 5 and 1 <= birth_date <= 20:
    print("You are Taurus!")
elif birth_month == 5 and 21 <= birth_date <= 31 or birth_month == 6 and 1 <= birth_date <= 20:
    print("You are Gemini!")
elif birth_month == 6 and 21 <= birth_date <= 30 or birth_month == 7 and 1 <= birth_date <= 22:
    print("You are Cancer!")
elif birth_month == 7 and 23 <= birth_date <= 31 or birth_month == 8 and 1 <= birth_date <= 22:
    print("You are Leo!")
elif birth_month == 8 and 23 <= birth_date <= 31 or birth_month == 9 and 1 <= birth_date <= 22:
    print("You are Virgo!")
elif birth_month == 9 and 23 <= birth_date <= 30 or birth_month == 10 and 1 <= birth_date <= 22:
    print("You are Libra!")
elif birth_month == 10 and 23 <= birth_date <= 31 or birth_month == 11 and 1 <= birth_date <= 22:
    print("You are Scorpio!")
elif birth_month == 11 and 23 <= birth_date <= 30 or birth_month == 12 and 1 <= birth_date <= 21:
    print("You are Sagittarius!")
elif birth_month == 12 and 22 <= birth_date <= 31 or birth_month == 1 and 1 <= birth_date <= 19:
    print("You are Capricorn!")
else:
    print("Invalid entry! Please, try again.")
