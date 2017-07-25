#A simple game to guess a randomly generated number. Difficulty can be set by the user.
import random
import os
import math

def clear_screen():                     #Function to clear the console screen
    clear = lambda:os.system('cls')
    clear()

def print_welcome_message():
    welcome_message = " Welcome to Guess The Number!! ".center(100, "_")
    print("\n", welcome_message, "\n")

def get_int_input():
    while True:
        try:
            return int(input())
        except :
            print("Invalid Input! Please try again.")
            continue

def get_difficulty_level():
    clear_screen()
    print_welcome_message()
    while True:
        print("Enter the respective number for difficulty:")
        difficulty_levels = list(difficulty_levels_values.keys())
        for level in range(len(difficulty_levels)):
            print("< {0} > {1}".format(level, difficulty_levels_values[difficulty_levels[level]]))
        selected_difficulty_index = get_int_input()
        if selected_difficulty_index not in range(len(difficulty_levels)):
            continue
        return difficulty_levels[selected_difficulty_index]

def get_lowest_difficulty_level():
    x = list(difficulty_levels_values.keys())
    x.sort()
    return x[0]

def get_random_number_in_range(selected_difficulty_level):
    return random.randint(0, selected_difficulty_level)

def print_low_high_message(user_input, random_number, selected_difficulty_level):
    if user_input - random_number > 0:
        word = "high"
    else:
        word = "low"

    if abs(user_input - random_number) <= selected_difficulty_level / 100:
        word = "Almost there! Still finely " + word
    elif abs(user_input - random_number) <= selected_difficulty_level / 50:
        word = "Minutely " + word
    elif abs(user_input - random_number) <= selected_difficulty_level / 20:
        word = "A bit " + word
    elif abs(user_input - random_number) <= selected_difficulty_level / 10:
        word = "Little " + word
    elif abs(user_input - random_number) <= selected_difficulty_level / 5:
        word = "Too " + word
    elif abs(user_input - random_number) <= selected_difficulty_level:
        word = "Extremely " + word
    else:
        word = "Haha! You're astronomically " + word
    print("{0}. Try again:".format(word))

def print_winner_message(step_count, selected_difficulty_level):
    min_steps_for_awesome = math.log(selected_difficulty_level, get_lowest_difficulty_level())
    print("Whoa! You're a champ! You guessed perferctly in {0} step{1}!!"
          .format("just " + str(step_count) if step_count <= min_steps_for_awesome else step_count,
          's' if step_count > 1 else ''))

def print_initial_input_message(selected_difficulty_level):
    print("Nice! Let's check your luck now. Enter your first guess (0 - {0:,}):".format(selected_difficulty_level))

def play_game():
    selected_difficulty_level = get_difficulty_level()

    random_number = get_random_number_in_range(selected_difficulty_level)
    # For testing purpose
    # print(random_number)

    print_initial_input_message(selected_difficulty_level)
    user_input = get_int_input()
    step_count = 1
    while user_input != random_number:
        print_low_high_message(user_input, random_number, selected_difficulty_level)
        user_input = get_int_input()
        step_count += 1
    print_winner_message(step_count, selected_difficulty_level)

#TODO make get_valid_y_n_opinion take a string as parameter to ask a question for input, or default question will be asked
#TODO put get_valid_y_n_opinion(), get_int_input() and other common functions in your own package


def get_valid_y_n_opinion():
    user_choice_options = ['y', 'n', 'yes', 'no']  # Taking most of the possible user inputs in cosideration
    user_choice_no_options = ['n', 'no']  # Until now, no need to define user_choice_yes_options list
    while True:
        user_choice = input()
        if user_choice.lower() not in user_choice_options:
            print("Wrong input. Please try again ( y / n ): ", end="")
            continue
        break
    if user_choice in user_choice_no_options:
        return False
    else:
        return True

def print_exit_message():
    exit_message = " Thank you for using this app. Developed by Nimesh Nischal. ".center(100, "-")
    print("\n", exit_message, "\n")
    input("Press enter to exit!")



#------------------ Main program ------------------#
difficulty_levels_values = { 10:"Noobie",
                             50:"Very Easy",
                             100:"Easy",
                             500:"Mediocre",
                             1000:"Good",
                             5000:"Hard",
                             10000:"Very Hard",
                             100000 : "Insane!!"}

while True:
    play_game()
    print("Play again? ( y / n ): ", end="")
    play_again_boolean = get_valid_y_n_opinion()
    if play_again_boolean:
        continue
    else:
        break
print_exit_message()

	
