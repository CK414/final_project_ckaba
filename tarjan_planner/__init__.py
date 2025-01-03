"""
tarjan_planner init module also containing the main module.
"""

from .relatives_manager import RelativesManager
from .transport_manager import TransportManager
from . import interface
from .logger import logger


def main():
    """
    Runs main program loop
    """

    # relatives_manager = RelativesManager("tarjan_planner/relatives.csv")
    # transport_manager = TransportManager("tarjan_planner/transport_modes.csv")
    print("-" * 40)
    print("Welcome to TarjanPlanner!")
    logger.info("Program started.")

    # Loop until quit selected by user.
    menu_quit = False
    while not menu_quit:
        interface.display_menu()
        user_input = input("Enter your choice: ")
        print("-" * 40)
        # Check user input conforms to desired inputs
        try:
            if (user_input := int(user_input)) == 0:
                logger.info("User selected to quit the program.")
                print("Exiting the program.")
                menu_quit = True
            elif 1 <= user_input <= 5:
                # Call the function associated with the chosen number
                interface.options[user_input]()
            else:
                logger.warning("User entered an invalid choice.")
                print("Invalid choice. Please select a number between 0 and 9.")
        except ValueError:
            # If the input can't be converted to an integer, print an error message.
            print("Invalid input. Please enter a number between 0 and 9.")
