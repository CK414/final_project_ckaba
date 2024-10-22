"""
Module containing all functions related to menu.
"""

import time
from .relatives_manager import RelativesManager
from .transport_manager import TransportManager

relatives_manager = RelativesManager("TarjanPlanner/relatives.csv")
transport_manager = TransportManager("TarjanPlanner/transport_modes.csv")


def display_menu():
    """
    Displays menu to user and waits for input.
    """
    print("Please select an option from the menu:")
    print("-" * 40)
    print("1. List Relatives")
    print("2. List Modes of Transport")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Option 5")
    print("6. Option 6")
    print("7. Option 7")
    print("8. Option 8")
    print("9. Option 9")
    print("0. Quit")
    print("-" * 40)


def option1():
    """
    Lists relatives and location data.
    """
    print("You selected Option 1: List Relatives")
    relatives_manager.list_relatives()
    print("Returning to Menu...")
    time.sleep(1.5)


def option2():
    """
    Lists transport data.
    """
    print("You selected Option 2: List Modes of Transport")
    transport_manager.list_transport()
    print("Returning to Menu...")
    time.sleep(1.5)


def option3():
    """
    .
    """
    print("You selected Option 3.")


def option4():
    """
    .
    """
    print("You selected Option 4.")


def option5():
    """
    .
    """
    print("You selected Option 5.")


def option6():
    """
    .
    """
    print("You selected Option 6.")


def option7():
    """
    .
    """
    print("You selected Option 7.")


def option8():
    """
    .
    """
    print("You selected Option 8.")


def option9():
    """
    .
    """
    print("You selected Option 9.")


options = {
    1: option1,
    2: option2,
    3: option3,
    4: option4,
    5: option5,
    6: option6,
    7: option7,
    8: option8,
    9: option9,
}