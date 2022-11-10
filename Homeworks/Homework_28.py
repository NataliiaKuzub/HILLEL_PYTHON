from datetime import datetime

db = input("Please, enter your date of birth in the format 'Year-Month-Day': ")

db_converted = datetime.strptime(db, '%Y-%m-%d')

print(f"You turned {(datetime.today() - db_converted).days} days today!")
