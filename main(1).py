from art import logo
import random

print(logo)

randomNumb = random.randint(1,100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

guessing = True

level = input("Chose a difficulty. Type 'easy' or 'hard':\n")
if level == "easy":
  attempts = 10
else:
  attempts = 5

print(f"You have {attempts} attempts remaining to guess the number.")

count = 0
while guessing:
  count += 1
  guess = int(input("Make a guess: "))
  if guess == randomNumb:
    print(f"You got it! The answer was {randomNumb}.")
    guessing = False
  elif count == attempts:
    print("You've run out of guesses, you lose.")
    guessing = False
  elif guess < randomNumb:
    print("Too low.")
    print(f"Remaining attempts: {attempts - count}") 
    print("Guess Again.")
  elif guess > randomNumb:
    print("Too high.")
    print(f"Remaining attempts: {attempts - count}")  
    print("Guess Again.")
   
 

