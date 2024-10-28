'''
Module containing all functions related to route planning.
'''

import networkx as nx
import matplotlib.pyplot as plt
from geopy.distance import geodesic
from .relatives_manager import RelativesManager
from .transport_manager import TransportManager

relatives_manager = RelativesManager("tarjan_planner/relatives.csv")
transport_manager = TransportManager("tarjan_planner/transport_modes.csv")

def draw_nodes():
    route_map = nx.Graph()

    for relative in relatives_manager.get_relatives():
        route_map.add_node(
            relative["Relative"],
            pos=(relative["Longitude"], relative["Latitude"])
        )

    pos = nx.get_node_attributes(route_map, 'pos')
    nx.draw(route_map, pos, with_labels=True)

    plt.show()
