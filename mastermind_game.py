def get_valid_number_input(prompt):
    while True:
        number = input(prompt)
        if number.isdigit() and len(number) == 4:
            return [int(d) for d in number]
        print("Invalid input! Please enter exactly 4 digits.")

def provide_feedback(guess, answer):
    correct_digits = 0
    current_digits = []

    for i in range(4):
        if guess[i] == answer[i]:
            correct_digits += 1
            current_digits.append(answer[i])
        else:
            current_digits.append("x")

    return correct_digits, current_digits

def play_game(player_num, answer):
    attempts = 0

    while True:
        attempts += 1
        guess = get_valid_number_input(f"Player {player_num}, enter your guess: ")
        correct_digits, current_digits = provide_feedback(guess, answer)

        if correct_digits == 4:
            print(f"Player {player_num} guessed the number in {attempts} attempts!")
            return attempts
        else:
            print(f"Not quite the number. You got {correct_digits} digits correct.")
            print(" ".join(map(str, current_digits)))

def main():
    print("Welcome to the Mastermind Game!")

    # Player 1 sets the number
    print("Player 1, set a 4-digit number for Player 2 to guess.")
    answer_p1 = get_valid_number_input("Player 1, enter your number: ")

    # Player 2 tries to guess the number
    attempts_p2 = play_game(2, answer_p1)

    # Player 2 sets the number
    print("Player 2, set a 4-digit number for Player 1 to guess.")
    answer_p2 = get_valid_number_input("Player 2, enter your number: ")

    # Player 1 tries to guess the number
    attempts_p1 = play_game(1, answer_p2)

    # Determine the winner
    if attempts_p1 < attempts_p2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts_p1 > attempts_p2:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie! Both players are equally matched.")

if __name__ == "__main__":
    main()
