"""
Module containing all functions related to menu.
"""

import time as tm
from geopy.distance import geodesic
from .relatives_manager import RelativesManager
from .transport_manager import TransportManager, TransportLinkManager
from .tarjan_planner import TarjanPlanner
from .logger import logger, clear_log_file

RELATIVES_FILE = "tarjan_planner/relatives.csv"
TRANSPORT_FILE = "tarjan_planner/transport_modes.csv"
LINKS_FILE = "tarjan_planner/transport_links.csv"

relatives_manager = RelativesManager(RELATIVES_FILE)
#transport_manager = TransportManager(TRANSPORT_FILE)
transport_manager = TransportLinkManager(TRANSPORT_FILE, LINKS_FILE)


# Menu #
def display_menu():
    """
    Displays menu to user and waits for input.
    """
    print("Please select an option from the menu:")
    print("-" * 40)
    print("1. List Relatives")
    print("2. List Modes of Transport")
    print("3. List Transport Links")
    print("4. Execute Route Planner")  # Run route planner
    # print("5. Compare transport modes between two relatives")
    print("5. Clear Log File")
    # print("7. Make Map")
    # print("8. Option 8")
    # print("9. Option 9")
    print("0. Quit")
    print("-" * 40)


# 1
def print_relatives():
    """
    Lists relatives and location data.
    """
    logger.info("User selected Option 1: List Relatives")
    relatives_manager.list_relatives()
    logger.info("Returning to Menu...")
    tm.sleep(1)


# 2
def print_transport():
    """
    Lists transport data.
    """
    logger.info("User selected Option 2: List Modes of Transport")
    transport_manager.list_transport()
    logger.info("Returning to Menu...")
    tm.sleep(1)

# 3
def print_links():
    """
    Lists possible transport links
    """
    logger.info("User selected Option 3: List Transport Links")
    transport_manager.list_links()
    logger.info("Returning to Menu...")
    tm.sleep(1)

# 4
def route_planner():
    """
    Runs the route planner to calculate the most efficient route through Seoul.
    """
    logger.info("User selected Option 4: Execute Route Planner")
    planner = TarjanPlanner(RELATIVES_FILE, TRANSPORT_FILE, LINKS_FILE)
    planner.create_graph()

    # Start at Tarjan's House
    start_node = "Yeoui-daero"
    
    best_route = []
    best_route = planner.find_best_route(
        start_node=start_node
    )
    planner.plot_graph(best_route)
    formatted_route = planner.format_route(best_route)
    logger.info("Best route based on travel time:\n%s", formatted_route)

    logger.info("Returning to Menu...")
    tm.sleep(1)


# 5
def compare_transport_methods():
    """
    Compares different transport methods between two selected relatives based on both time and cost.
    """
    logger.info("User selected Option 5: Compare Transport Methods")
    planner = TarjanPlanner(RELATIVES_FILE, TRANSPORT_FILE, LINKS_FILE)
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
    relative1_street = relatives[relative1_index - 1]["Street Name"]
    relative2 = relatives[relative2_index - 1]["Relative"]
    relative2_street = relatives[relative2_index - 1]["Street Name"]

    # Calculate and display the comparison of different transport methods
    print(f"Comparison of transport methods between {relative1} ({relative1_street}) and {relative2} ({relative2_street}):")
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


# 6
def clear_log():
    """
    Clears all data in the logger file.
    """
    logger.info("User selected Option 6: Clear Log File")
    clear_log_file()
    print("Log file cleared.")
    logger.info("Returning to Menu...")
    tm.sleep(1)


# 7
def make_map():

    print("You selected Option 7: Make Map")
    planner = TarjanPlanner(RELATIVES_FILE, TRANSPORT_FILE, LINKS_FILE)
    planner.create_graph()
    planner.plot_graph()


# def option8():

#     print("You selected Option 8.")


# def option9():

#     print("You selected Option 9.")

options = {
    1: print_relatives,
    2: print_transport,
    3: print_links,
    4: route_planner,
    #5: compare_transport_methods,
    5: clear_log,
    #7: make_map,
    # 8: option8,
    # 9: option9,
}
