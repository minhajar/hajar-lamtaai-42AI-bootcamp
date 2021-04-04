#GuessGame
import random


num=random.randint(1,99)
attempts=0
guess=None
while guess!=num:

        print("""This is an interactive guessing game!
        You have to enter a number between 1 and 99 to find out the secret number.
        Type 'exit' to end the game.
        Good luck!
        What's your guess between 1 and 99?""")
        guess=(input())
        if guess=="exit":
            print("Goodbye")
            break
        
        elif guess<num:
            print("too low!")
        elif guess>num:
            print("too high!")
        elif guess==str:
            print("it's not a number")
        elif guess==num:
            print("""Congratulations, you've got it!\n
                   You won in""",attempts,"""attempts!""")
        attempts+=1
        if attempts==1:
            print("""The answer to the ultimate question of life, the universe and everything is""",num,
                 
                    """Congratulations! You got it on your first try!""")
