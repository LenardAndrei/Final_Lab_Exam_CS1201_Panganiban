import random
from datetime import datetime

class DiceRollGame:

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.stage = 1
        self.total_score = 0
        self.round = 0
        self.stage_win = 0

    def register(self):
        try:
            with open('accounts.txt', 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            lines = []

        print("Registration")
        self.username = input("Create username (at least 4 characters): ")
        
        if len(self.username) < 4:
            print("Username must be at least 4 characters")
            return
        else:
            self.password = input("Create password (at least 8 characters): ")
            if len(self.password) < 8:
                print("Password must be at least 8 characters")
                return
            elif any(self.username in line for line in lines):
                print("Username already exists")
                return
            else:
                with open('accounts.txt', 'a') as file:
                    file.write(f"Username: {self.username} Password: {self.password}\n")
                print("Registration successful")
                      

    def login(self):
        print("")
        print("Login")
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")

        try:
            with open('accounts.txt', 'r') as file:
                for line in file:
                    if f"Username: {self.username} Password: {self.password}" in line:
                        print("Logged In!")
                        DiceRollGame.login_menu(self)    
                        break
                else:
                    print("User not found or wrong password")
        except FileNotFoundError:
            print("No existing account")    


    def roll_dice(self):
        return random.randint(1, 6)
    
    def play_round(self):
        player_roll = self.roll_dice()
        computer_roll = self.roll_dice()

        print("You rolled:", player_roll)
        print("CPU rolled: ", computer_roll)

        if player_roll > computer_roll:
            print("You win this round!")
            self.player_score += 1

        elif player_roll < computer_roll:
            print("CPU wins this round!")
            self.computer_score += 1

        else:
            print("It's a tie!")

        print(f"{self.username} Score:", self.player_score)
        print("CPU score:", self.computer_score)
        print()


    def play_game(self):
        print("\nWelcome to Dice Roll Game!")
        print(f"Stage:", self.stage)
        print(f"{self.username} is playing")

        while self.round < 3:
            input("Press enter to roll the dice...")
            self.round += 1
            self.play_round()

        if self.player_score > self.computer_score:
            while True:
                try:
                    print("Congratulations! You win!")
                    print("You earn extra 3 points!")
                    self.total_score += self.player_score
                    self.total_score += 3
                    self.stage_win += 1
                    print(f"{self.username} total score: {self.total_score} Stage won: {self.stage_win}")
                    choice = int(input("Do you want to continue to next stage? Press 1 (Yes) or 2 (No): "))
                    if choice == 1:
                        self.stage += 1
                        self.player_score -= self.player_score
                        self.computer_score -= self.computer_score
                        self.round -= 3
                        DiceRollGame.play_game(self)
                        break
                    if choice == 2:
                        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        with open('scores.txt', 'a') as score_file:
                            score_file.write(f"Date/Time: {current_datetime}, Username: {self.username}, Total Score: {self.total_score}, Stage Win: {self.stage_win}\n")
                        
                        self.player_score -= self.player_score
                        self.computer_score -= self.computer_score
                        self.total_score -= self.total_score
                        self.round -= 3
                        self.stage = 1
                        self.login_menu()
                        break
                    else:
                        print("Invalid input. Please try again.")
                except ValueError:
                    print("Invalid input. Please try again.")
        
        elif self.player_score < self.computer_score:
            while True:
                try:
                    print(f"You lost this stage {self.username}.")
                    self.total_score += self.player_score
                    print(f"{self.username} total score: {self.total_score} Stage won: {self.stage_win}")
                    choice = int(input("Do you want to play again? Press 1 (Yes) or 2 (No): "))
                    if choice == 1:
                        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        with open('scores.txt', 'a') as score_file:
                            score_file.write(f"Date/Time: {current_datetime}, Username: {self.username}, Total Score: {self.total_score}, Stage Win: {self.stage_win}\n")
                        
                        self.player_score -= self.player_score
                        self.computer_score -= self.computer_score
                        self.round -= 3
                        self.total_score -= self.total_score
                        self.stage = 1
                        self.stage_win = 0
                        DiceRollGame.play_game(self)
                        break
                    if choice == 2:
                        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        with open('scores.txt', 'a') as score_file:
                            score_file.write(f"Date/Time: {current_datetime}, Username: {self.username}, Total Score: {self.total_score}, Stage Win: {self.stage_win}\n")
                        
                        self.player_score -= self.player_score
                        self.computer_score -= self.computer_score
                        self.round -= 3
                        self.total_score -= self.total_score
                        self.stage = 1
                        self.stage_win = 0
                        self.login_menu()
                        break
                    else:
                        print("Invalid input. Please try again.")
                except ValueError:
                    print("Invalid input. Please try again.")

        else:
            while True:
                try:
                    print("It's a tie!")
                    print(f"{self.username} total score: {self.total_score} Stage won: {self.stage_win}")
                    choice = int(input("Do you want to play again? Press 1 (Yes) or 2 (No): "))
                    if choice == 1:
                        self.player_score -= self.player_score
                        self.computer_score -= self.computer_score
                        self.round -= 3
                        DiceRollGame.play_game(self)
                        break
                    if choice == 2:
                        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        with open('scores.txt', 'a') as score_file:
                            score_file.write(f"Date/Time: {current_datetime}, Username: {self.username}, Total Score: {self.total_score}, Stage Win: {self.stage_win}\n")
                        
                        self.player_score -= self.player_score
                        self.computer_score -= self.computer_score
                        self.round -= 3
                        self.stage = 1
                        self.total_score -= self.total_score
                        self.stage_win = 0
                        self.login_menu()
                        break
                    else:
                        print("Invalid input. Please try again.")
                except ValueError:
                    print("Invalid input.Please try again.")
    

    def top_scores(self):
        try:
            with open('scores.txt', 'r') as file:
                lines = file.readlines()

            scores = []
            for line in lines:
                parts = line.split(", ")
                datetime_str = parts[0].split(": ")[1].strip()
                datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
                username = parts[1].split(": ")[1].strip()
                total_score = int(parts[2].split(": ")[1].strip())
                stage_win = int(parts[3].split(": ")[1].strip())
                scores.append((datetime_obj, username, total_score, stage_win))

            sorted_scores = sorted(scores, key=lambda x: x[2], reverse=True)

            print("\nTop Scores")
            print("Rank\tDate/Time\t\t\tUsername\tScore\t\tStage Win")
            for i, (datetime_obj, username, total_score, stage_win) in enumerate(sorted_scores[:10], 1):
                print(f"{i}\t{datetime_obj}\t\t{username}\t\t{total_score}\t\t{stage_win}")

        
            input("\n\nPress enter to go back...")
            self.login_menu()

        except FileNotFoundError:
            print("No games played yet. Play a game to see top scores.")
            input("\nPress enter to go back...")
            self.login_menu()


    def login_menu(self):
        while True:
            try:
                print("\nLog in Menu")
                print("1. Start Game")
                print("2. Show Top Scores")
                print("3. Log out")

                choice = int(input("Enter your choice: "))
                
                if choice == 1:
                   self.play_game()
                   break
                if choice == 2:
                   self.top_scores()
                   break
                if choice == 3:
                   print("Logging out")
                   return 
                else:
                    print("Invalid input. Please try again.")

            except ValueError:
                print("Invalid input. Please try again.")

