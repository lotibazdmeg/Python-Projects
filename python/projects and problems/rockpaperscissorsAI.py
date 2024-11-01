import random

print("Hey and welcome to Rock-Paper-Scissors! I'm guessing you're not braindead, so I don't have to explain the game to you. Enjoy!\n")

def main():
    running = True
    rps_list = ["Rock", "Paper", "Scissors"]
    while running:
        computer_choice = random.choice(rps_list)
        player_choice = input(f"    Rock, Paper, Scissors!:\n        ")
        print("         vs")
        print(f"\t{computer_choice}")

        if player_choice == computer_choice:
            print("     It's a tie!")
        elif (player_choice == "Rock" and computer_choice == "Scissors") or (player_choice == "Paper" and computer_choice == "Rock") or (player_choice == "Scissors" and computer_choice == "Paper"):
            print("     Player 1 won! Still a loser.")
        else:
            print("     Player 1 lost! What a loser.")

        play_again = input("    Want to play again? ").lower()
        if play_again == 'yes':
            continue
        elif play_again == "no":
            break
        else:
            print("     I don't understand that bozo.")

main()