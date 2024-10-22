# Rename to __main__.py before submission...
from display_menu import display_menu

def main():
    print("-" * 40)
    print("Welcome to TarjanPlanner!")
    
    # Loop until quit selected by user.
    quit = False
    while not quit:
        display_menu()
        user_input = input("Enter your choice: ")
        print("-" * 40)
        
        try:
            user_input = int(user_input)
            if user_input == 0:
                print("You selected Quit. Exiting the program.")
                quit = True
            elif 1 <= user_input <= 9:
                print(f"You selected Option {user_input}.")
            else:
                print("Invalid choice. Please select a number between 0 and 9.")
        except:
            # If the input can't be converted to an integer, print an error message.
            print("Invalid input. Please enter a number between 0 and 9.")

        

if __name__ == "__main__":
    main()