import random

number = random.randint(1,15)
player_name = input("What is your name: ")
number_of_guess = 0

print("Welcome " + player_name + ", this is a guessing game where you need to guess from 1 to 15:")

while number_of_guess <5:
    guess = int(input())
    number_of_guess += 1
    if guess < number:
        print("Your guess is a bit low :c")
    if guess > number:
        print("Your guess is a bit too high, buddy!")
    if guess == number:
        break

if guess == number:
    print("You guess in " + str(number_of_guess) + " tries!")
else:
    print("Unfortunately, you didn't guess the number correctly, the number is " + str(number))