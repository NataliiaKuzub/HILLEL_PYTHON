from datetime import datetime

week_days = {
    0: "Понеділок",
    1: "Вівторок",
    2: "Середа",
    3: "Четвер",
    4: "П'ятниця",
    5: "Субота",
    6: "Неділя"
}

d = input("Please, enter the date in the format 'Year-Month-Day': ")

# Printing day of the week in Ukrainian
print(f"День тижня: {week_days[datetime.strptime(d, '%Y-%m-%d').weekday()]}")

# Printing day of the week in English
print(f"The day of the week: {datetime.strptime(d, '%Y-%m-%d').strftime('%A')}")
