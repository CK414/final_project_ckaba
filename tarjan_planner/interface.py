"""
Module containing all functions related to menu.
"""

import time as tm
from geopy.distance import geodesic
from .relatives_manager import RelativesManager
from .transport_manager import TransportManager
from .tarjan_planner import TarjanPlanner
from .logger import logger, clear_log_file

relatives_file = "tarjan_planner/relatives.csv"
transport_file = "tarjan_planner/transport_modes.csv"

relatives_manager = RelativesManager(relatives_file)
transport_manager = TransportManager(transport_file)


def display_menu():
    """
    Displays menu to user and waits for input.
    """
    print("Please select an option from the menu:")
    print("-" * 40)
    print("1. List Relatives")
    print("2. List Modes of Transport")
    print("3. Execute Route Planner")  # Run route planner
    print("4. Compare transport modes between two relatives")
    print("5. Clear Log File")
    # print("6. Option 6")
    # print("7. Option 7")
    # print("8. Option 8")
    # print("9. Option 9")
    print("0. Quit")
    print("-" * 40)


def print_relatives():
    """
    Lists relatives and location data.
    """
    logger.info("User selected Option 1: List Relatives")
    relatives_manager.list_relatives()
    logger.info("Returning to Menu...")
    tm.sleep(1)


def print_transport():
    """
    Lists transport data.
    """
    logger.info("User selected Option 2: List Modes of Transport")
    transport_manager.list_transport()
    logger.info("Returning to Menu...")
    tm.sleep(1)


def route_planner():
    """
    Runs the route planner to calculate the most efficient route through Seoul.
    """
    logger.info("User selected Option 3: Execute Route Planner")
    planner = TarjanPlanner(relatives_file, transport_file)
    planner.create_graph()

    # Prompt the user to choose the criterion
    criterion = input("Choose option for route planning (time/cost): ").strip().lower()
    if criterion not in ["time", "cost"]:
        logger.warning("Invalid option entered. Defaulting to 'time'.")
        criterion = "time"

    planner.plot_graph(criterion=criterion)
    best_route, transport_methods, durations = planner.find_best_route(
        start_node="Relative_1", criterion=criterion
    )
    formatted_route = planner.format_route(best_route, transport_methods, durations)
    logger.info(f"Best route based on {criterion}:\n{formatted_route}")

    logger.info("Returning to Menu...")
    tm.sleep(1)


def compare_transport_methods():
    """
    Compares different transport methods between two selected relatives based on both time and cost.
    """
    logger.info("User selected Option 4: Compare Transport Methods")
    planner = TarjanPlanner(relatives_file, transport_file)
    planner.create_graph()

    # Prompt the user to enter two integers corresponding to the relatives
    try:
        relative1_index = int(
            input("Enter the number corresponding to the first relative: ")
        )
        relative2_index = int(
            input("Enter the number corresponding to the second relative: ")
        )
    except ValueError:
        logger.warning("Invalid input. Please enter valid integers.")
        print("Invalid input. Please enter valid integers.")
        return

    relatives = planner.relatives_manager.get_relatives()
    if (
        relative1_index < 1
        or relative1_index > len(relatives)
        or relative2_index < 1
        or relative2_index > len(relatives)
    ):
        logger.warning("Invalid relative numbers entered.")
        print("Invalid relative numbers entered. Please try again.")
        return

    relative1 = relatives[relative1_index - 1]["Relative"]
    relative2 = relatives[relative2_index - 1]["Relative"]

    # Calculate and display the comparison of different transport methods
    print(f"Comparison of transport methods between {relative1} and {relative2}:")
    for transport in planner.transport_manager.get_transport():
        distance = geodesic(
            (
                float(relatives[relative1_index - 1]["Latitude"]),
                float(relatives[relative1_index - 1]["Longitude"]),
            ),
            (
                float(relatives[relative2_index - 1]["Latitude"]),
                float(relatives[relative2_index - 1]["Longitude"]),
            ),
        ).km
        speed = float(transport["Speed_kmh"])
        cost = float(transport["Cost_per_km"]) * distance
        time = distance / speed + float(transport["Transfer_Time_min"]) / 60
        print(f"Transport Method: {transport['Mode of Transport']}")
        print(f"Time: {time:.2f} hours")
        print(f"Cost: {cost:.2f} currency units")
        print("-" * 40)

    logger.info("Returning to Menu...")
    tm.sleep(1)


def clear_log():
    """
    Clears all data in the logger file.
    """
    logger.info("User selected Option 5: Clear Log File")
    clear_log_file()
    print("Log file cleared.")
    logger.info("Returning to Menu...")
    tm.sleep(1)


"""
def option6():

    print("You selected Option 6.")


def option7():

    print("You selected Option 7.")


def option8():

    print("You selected Option 8.") 


def option9():

    print("You selected Option 9.")
"""

options = {
    1: print_relatives,
    2: print_transport,
    3: route_planner,
    4: compare_transport_methods,
    5: clear_log,
    # 6: option6,
    # 7: option7,
    # 8: option8,
    # 9: option9,
}
