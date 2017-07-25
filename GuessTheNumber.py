#A simple game to guess a randomly generated number. Difficulty can be set by the user.
import nimesh_app_basics
import math


def get_difficulty_level():
    nimesh_app_basics.clear_screen()
    nimesh_app_basics.print_welcome_message(app_name)
    difficulty_levels = list(difficulty_levels_values.keys())
    for level in range(len(difficulty_levels)):
        print("< {0} > {1}".format(level, difficulty_levels_values[difficulty_levels[level]]))
    while True:
        selected_difficulty_index = nimesh_app_basics.get_int_input("Enter the respective number for difficulty:")
        if selected_difficulty_index not in range(len(difficulty_levels)):
            print("Please enter a valid number.")
            continue
        return difficulty_levels[selected_difficulty_index]


def get_lowest_difficulty_level():
    x = list(difficulty_levels_values.keys())
    x.sort()
    return x[0]


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
    print("\nWhoa! You're a champ! You guessed perfectly in {0} step{1}!!"
          .format("just " + str(step_count) if step_count <= min_steps_for_awesome else step_count,
          's' if step_count > 1 else ''))


def print_initial_input_message(selected_difficulty_level):
    print("\nNice! Let's check your luck now. Enter your first guess (0 - {0:,}):".format(selected_difficulty_level))


def play_game():
    selected_difficulty_level = get_difficulty_level()

    random_number = nimesh_app_basics.get_random_int_in_range(0,selected_difficulty_level)
    # For testing purpose
    # print(random_number)

    print_initial_input_message(selected_difficulty_level)
    user_input = nimesh_app_basics.get_int_input("")
    step_count = 1
    while user_input != random_number:
        print_low_high_message(user_input, random_number, selected_difficulty_level)
        user_input = nimesh_app_basics.get_int_input("")
        step_count += 1
    print_winner_message(step_count, selected_difficulty_level)


# ------------------ Main program ------------------ #
difficulty_levels_values = { 10:"Noobie",
                             50:"Very Easy",
                             100:"Easy",
                             500:"Mediocre",
                             1000:"Good",
                             5000:"Hard",
                             10000:"Very Hard",
                             100000 : "Insane!!"}

app_name = "Guess The Number"

while True:
    play_game()
    play_again_boolean = nimesh_app_basics.get_valid_y_n_opinion("Play again? ( y / n ): ")
    if play_again_boolean:
        continue
    else:
        break

nimesh_app_basics.print_exit_message(app_name)

	
