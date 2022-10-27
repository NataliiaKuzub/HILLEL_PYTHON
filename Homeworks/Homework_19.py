import random

the_number = random.randrange(0, 100)
#  print(the_number)

print("Guess the number from 0 to 100: ")
guess = int(input("Please, enter the number: "))
n = 1
while guess != the_number:
    n += 1
    if guess > the_number:
        print("The number is too big.")
    else:
        print("The number is too small.")
    guess = int(input("Please, enter the number: "))

print(f"Correct, you've got the number after {n}th try! It was {the_number}.")
