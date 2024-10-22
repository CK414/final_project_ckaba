# pylint: disable=invalid-name
"""
Documentation
"""
from .relatives_manager import RelativesManager
from .transport_manager import TransportManager
from . import menu


def main():
    """
    Runs main program loop
    """

    relatives_manager = RelativesManager("TarjanPlanner/relatives.csv")
    transport_manager = TransportManager("TarjanPlanner/transport_modes.csv")
    print("-" * 40)
    print("Welcome to TarjanPlanner!")

    # Loop until quit selected by user.
    menu_quit = False
    while not menu_quit:
        menu.display_menu()
        user_input = input("Enter your choice: ")
        print("-" * 40)
        # Check user input conforms to desired inputs
        try:
            if (user_input := int(user_input)) == 0:
                print("You selected Quit. Exiting the program.")
                menu_quit = True
            elif 1 <= user_input <= 9:
                # Call the function associated with the chosen number
                menu.options[user_input]()
            else:
                print("Invalid choice. Please select a number between 0 and 9.")
        except ValueError:
            # If the input can't be converted to an integer, print an error message.
            print("Invalid input. Please enter a number between 0 and 9.")
