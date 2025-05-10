"""
Write in pseudocode and then in Python a program that simulates a guessing game. The program should randomly choose a number between 1 and 100. The user must guess the number, and the program will tell the user if their guess is too high, too low, or correct. The game should continue until the user guesses the correct number or chooses to quit. The program should also keep track of how many guesses the user made.
"""

"""
First the program will randomly choose a number
then it will ask the user for their guess
then it will go into a loop with an if statement that check to see if the number is correct
if it's correct, it will exit the loop and print 'congrats, you got it right!'
if they guess wrong, it will tell them they guessed wrong, ask if they want to try again, and restart the loop if they do
if they dont, it will exit the loop, end the program and say 'thanks for playing!'
"""
import random

def guessing_game():
    print("Let's play a game, shall we...")
    computer_number = random.randint(1, 100)
    print('I have thought of a number between 1 and 100. Can you guess it?')
    user_guess = (int(input('What do you think the number is? ')))
    keep_going = True

    while keep_going == True:
        if user_guess == computer_number:
            print('You got it right! congrats!')
            keep_going = False
            print('Do you want to play again? (y/n)')
            play_again = input()
            if play_again == "y":
                guessing_game()
            else:
                print('thanks for playing!')
        else:
            print('Aww tough luck you guessed wrong this time... do you want to try again? (y/n)')
            try_again = input()
            if try_again == "y":
                print('Alright, what is your guess this time?')
                user_guess = input()
            else:
                print('Thanks for playing, better luck next time!')
                keep_going = False

guessing_game()