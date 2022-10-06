while True:
    valid = False
    while not valid:
        try:
            birth_month = int(input("Please, enter your month of birth (as a number from 1 to 12): "))
            birth_date = int(input("Please, enter your date of birth: "))
            valid = True
        except ValueError:
            print("Invalid entry. Please, try again.")

    if birth_month > 12 or birth_month < 1 or birth_date < 1:
        print("Invalid entry. Please, try again.")
        continue
    elif birth_month == 1:
        if birth_date < 20:
            print("You are Capricorn!")
            break
        elif birth_date < 32:
            print("You are Aquarius!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
    elif birth_month == 2:
        if birth_date < 19:
            print("You are Aquarius!")
            break
        elif birth_date < 30:
            print("You are Pisces!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
    elif birth_month == 3:
        if birth_date < 21:
            print("You are Pisces!")
            break
        elif birth_date < 32:
            print("You are Aries!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
    elif birth_month == 4:
        if birth_date < 20:
            print("You are Aries!")
            break
        elif birth_date < 31:
            print("You are Taurus!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
    elif birth_month == 5:
        if birth_date < 21:
            print("You are Taurus!")
            break
        elif birth_date < 32:
            print("You are Gemini!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
    elif birth_month == 6:
        if birth_date < 21:
            print("You are Gemini!")
            break
        elif birth_date < 31:
            print("You are Cancer!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
    elif birth_month == 7:
        if birth_date < 23:
            print("You are Cancer!")
            break
        elif birth_date < 32:
            print("You are Leo!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
    elif birth_month == 8:
        if birth_date < 23:
            print("You are Leo!")
            break
        elif birth_date < 32:
            print("You are Virgo!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
    elif birth_month == 9:
        if birth_date < 23:
            print("You are Virgo!")
            break
        elif birth_date < 31:
            print("You are Libra!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
    elif birth_month == 10:
        if birth_date < 23:
            print("You are Libra!")
            break
        elif birth_date < 32:
            print("You are Scorpio!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
    elif birth_month == 11:
        if birth_date < 22:
            print("You are Scorpio!")
            break
        elif birth_date < 31:
            print("You are Sagittarius!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
    else:
        if birth_date < 22:
            print("You are Sagittarius!")
            break
        elif birth_date < 32:
            print("You are Capricorn!")
            break
        else:
            print("Invalid entry. Please, try again.")
            continue
