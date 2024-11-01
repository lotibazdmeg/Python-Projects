import random

print("Welcome to the random number guessing game\nYou have to guess a number between 1 and 100.\nGood luck!")

guess = int(input("Chooes a number between 1 and 100: "))
randomnumber = random.randint(0, 100)

while True:
    
     if guess == randomnumber:
        print("You won, congrats'!")
        break
     elif guess > randomnumber:
        print("Too high")
        guess = int(input("Chooes a number between 1 and 100: "))
     elif guess < randomnumber:
        print("Too low")
        guess = int(input("Chooes a number between 1 and 100: "))