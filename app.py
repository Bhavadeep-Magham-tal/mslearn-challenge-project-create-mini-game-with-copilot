import random

# write 'hello world' to the console
print('hello world')

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            return True
        elif play_again == 'no':
            return False
        else:
            print("Invalid choice. Please try again.")

def display_score(score):
    print(f"Your score: {score}")

def play_game():
    rounds_played = 0
    rounds = []
    score = 0
    winning_rounds = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            score += 1
            winning_rounds += 1
        rounds_played += 1
        rounds.append((user_choice, computer_choice, result, rounds_played))
        display_score(score)
        if not play_again():
            print("Game terminated. Your final score is:", score, "Number of rounds played:", rounds_played)
            print("Number of winning rounds:", winning_rounds)
            print("Rounds:")
            for round in rounds:
                print(f"Round: {round[3]}-- User choice: {round[0]}, Computer choice: {round[1]}, Result: {round[2]}")
            break

if __name__ == "__main__":
    play_game()


