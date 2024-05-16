from utils.diceroll import DiceRollGame

def main_menu():
        dc = DiceRollGame()
     
        while True:
            try:
                print("")
                print("Welcome to Dice Roll Game!")
                print("1. Register")
                print("2. Log In")
                print("3. Exit")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    dc.register()
                    main_menu()
                    break
                elif choice == 2:
                    dc.login()
                    main_menu()
                    break
                elif choice == 3:
                    print("Exiting..")
                    quit()
                else:
                    print("Invalid input. Please try again.")

            except ValueError:
                print("Invalid input. Please try again.")
