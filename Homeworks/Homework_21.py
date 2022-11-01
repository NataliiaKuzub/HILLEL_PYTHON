zodiac = {
    "овен": '21.03-20.04',
    "тілець": '21.04-21.05',
    "близнята": '22.05-21.06',
    "рак": '22.06-22.07',
    "лев": '23.07-22.08',
    "діва": '23.08-23.09',
    "терези": '24.09-23.10',
    "скорпіон": '24.10-22.11',
    "стрілець": '23.11-21.12',
    "козоріг": '22.12-20.01',
    "водолій": '21.01-18.02',
    "риби": '19.02-20.03',
}

days_in_month = {
    1: 31,
    2: 29,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

birth_month = int(input("Please, enter your month of birth (as a number from 1 to 12): "))
birth_date = int(input("Please, enter your date of birth: "))

if birth_month not in days_in_month or \
        birth_date > days_in_month[birth_month] or \
        birth_date < 1:
    print("Invalid entry! Please, try again.")
else:
    for key in zodiac:
        for n, i in enumerate(zodiac[key].split('-')):
            dates = [int(k) for k in i.split('.')]
            if dates[1] == birth_month:
                if n == 0 and birth_date >= dates[0]:
                    print(f"You are {key}!")
                elif n == 1 and birth_date <= dates[0]:
                    print(f"You are {key}!")
