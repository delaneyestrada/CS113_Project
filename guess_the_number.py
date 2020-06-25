# Guess The Number game coding project for study.com class Computer Science 113: Programming in Python.

# imports random module
import random


# displays title and requirements for the program
def display_title():
    print("Guess The Number Game\n\nThe program should consist of three functions. The first will display the Title and "
          "program specifications.\nThe second plays the game. The main function calls those functions as it controls " 
          "the playing of the game.\nThe Python program should be developed in three steps and each step builds off the "
          "code from the previous step.")


# creates the function for the logic of the game
def play_game():
    # creates a variable with a random number
    random_number = random.randint(1, 10)

    # loop allowing the user to guess the number until they get it correct
    while True:
        # keep looping if user gives a non integer value
        while True:
            user_number = input("\nGuess a number between 1 and 10:\n")
            try:
                # attempt to cast input variable as an integer
                user_number = int(user_number)
                # if no exceptions break from while loop
                break
            # catch ValueError exception if input is not an integer
            except ValueError:
                print("Please enter a whole number")

        if user_number < random_number:
            print("Too low")
        elif user_number > random_number:
            print("Too high")
        else:
            print("You guessed it")
            # returns to main() function
            return


# creates main function that controls the flow of the program
def main():
    # variable set to yes by default so that game plays on first loop
    play_again = "yes"
    display_title()
    # loop while user answers "yes" to play again
    while play_again == "yes":
        play_game()
        # prompt user to play again or exit the game and convert to lowercase
        play_again = input("\nEnter 'yes' to play again. Enter anything else to exit the game.\n").lower()


# calls the main function
main()
