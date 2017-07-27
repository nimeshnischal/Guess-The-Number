import os
import random


# Function to clear the console screen
def clear_screen():
    clear = lambda:os.system('cls')
    clear()


def print_welcome_message(app_name):
    welcome_message = " Welcome to {0}!! ".format(
     "an App developed by Nimesh Nischal (aka NMZ)"
        if app_name is None else app_name
    ).center(100, "_")
    print("\n", welcome_message, "\n")


def get_int_input(input_message):
    if input_message is None:
        print("Please provide an integer input: ", end="")
    else:
        print(input_message, end="")
    while True:
        try:
            return int(input())
        except ValueError :
            print("Invalid Input! Please try again: ", end="")
            continue
        except KeyboardInterrupt:
            exit()


def get_non_empty_string_input(input_message, error_message):
    try:
        x = input("Please enter a non-empty string: " if input_message is None else input_message)
    except KeyboardInterrupt:
        exit()
    else:
        if x == "":
            print("Invalid Input! A non-empty string please."
                                  if error_message is None else error_message)
            return get_non_empty_string_input(input_message, error_message)
        else:
            return x


# Function to generate a random number between two numbers, including those two numbers
def get_random_int_in_range(min_num, max_num):
    return random.randint(min_num,max_num)


def get_valid_y_n_opinion(input_message):
    # Taking most of the possible yes no user inputs in consideration
    user_choice_options = ['y', 'n', 'yes', 'no']
    # Until now, no need to define user_choice_yes_options list
    user_choice_no_options = ['n', 'no']
    if input_message is None:
        print("Please provide an input: ( y / n ): ", end="")
    else:
        print(input_message, end="")
    while True:
        user_choice = input()
        if user_choice.lower() not in user_choice_options:
            print("Wrong input. Please try again ( y / n ): ", end="")
            continue
        break
    if user_choice.lower() in user_choice_no_options:
        return False
    else:
        return True


def print_exit_message(app_name):
    exit_message = " Thank you for using {0}. Developed by Nimesh Nischal (aka NMZ). ".format(
        "this app" if app_name is None else app_name
    ).center(100, "-")
    print("\n", exit_message, "\n")
    input("Press enter to exit!")