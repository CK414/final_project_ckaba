"""
Module containing all functions related to route planning.
"""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from geopy.distance import geodesic
from networkx.algorithms import approximation as approx
from .relatives_manager import RelativesManager
from .transport_manager import TransportManager
from .logger import logger, log_execution_time


class TarjanPlanner:
    '''
    Class Containing all functions related to calculating the best route for Tarjan.
    '''
    def __init__(self, relatives_file, transport_file):
        self.relatives_manager = RelativesManager(relatives_file)
        self.transport_manager = TransportManager(transport_file)
        self.route_map = nx.Graph()

    def create_graph(self):
        """
        Create a graph with relatives as nodes and edges based on transport modes.
        """
        relatives = self.relatives_manager.get_relatives()
        transport_modes = self.transport_manager.get_transport()

        # Add nodes for each relative
        for relative in relatives:
            self.route_map.add_node(
                relative["Relative"],
                pos=(float(relative["Latitude"]), float(relative["Longitude"])),
            )

        # Add edges based on transport modes
        for i, relative1 in enumerate(relatives):
            for j, relative2 in enumerate(relatives):
                if i != j:
                    distance = geodesic(
                        (float(relative1["Latitude"]), float(relative1["Longitude"])),
                        (float(relative2["Latitude"]), float(relative2["Longitude"])),
                    ).km
                    for transport in transport_modes:
                        speed = float(transport["Speed_kmh"])
                        cost = float(transport["Cost_per_km"]) * distance
                        travel_time = (
                            distance / speed
                            + float(transport["Transfer_Time_min"]) / 60
                        )
                        self.route_map.add_edge(
                            relative1["Relative"],
                            relative2["Relative"],
                            travel_time=travel_time,
                            cost=cost,
                            transport=transport["Mode of Transport"],
                        )
                        logger.debug(
                            "Edge from %s to %s by %s: time=%.2f, cost=%.2f",
                            relative1['Relative'],
                            relative2['Relative'],
                            transport['Mode of Transport'],
                            travel_time,
                            cost
                        )

    @log_execution_time
    def find_best_route(self, start_node, criterion="time"):
        """
        Find the best route based on the given criterion (time or cost) using TSP solver.
        """
        if criterion == "time":
            weight = "travel_time"
        elif criterion == "cost":
            weight = "cost"
        else:
            raise ValueError("Invalid criterion. Choose 'time' or 'cost'.")

        # Solve the TSP
        path = approx.traveling_salesman_problem(self.route_map, weight, cycle=False)

        # Ensure the path starts at the start_node
        start_index = path.index(start_node)
        path = path[start_index:] + path[:start_index]

        # Get the transport methods and durations for each leg
        transport_methods = []
        durations = []
        for i in range(len(path) - 1):
            edge_data = self.route_map.get_edge_data(path[i], path[i + 1])
            transport_methods.append(edge_data["transport"])
            # Calculate duration based on the selected criterion
            if criterion == "time":
                durations.append(edge_data["travel_time"])
            else:
                distance = geodesic(
                    (
                        float(self.route_map.nodes[path[i]]["pos"][0]),
                        float(self.route_map.nodes[path[i]]["pos"][1]),
                    ),
                    (
                        float(self.route_map.nodes[path[i + 1]]["pos"][0]),
                        float(self.route_map.nodes[path[i + 1]]["pos"][1]),
                    ),
                ).km
                speed = float(
                    self.transport_manager.get_transport_by_mode(
                        edge_data["transport"]
                    )["Speed_kmh"]
                )
                transfer_time = (
                    float(
                        self.transport_manager.get_transport_by_mode(
                            edge_data["transport"]
                        )["Transfer_Time_min"]
                    )
                    / 60
                )
                durations.append(distance / speed + transfer_time)
            logger.debug(
                "Leg from %s to %s by %s: %s=%.2f",
                path[i],
                path[i + 1],
                edge_data['transport'],
                weight, edge_data[weight]
            )

        return path, transport_methods, durations

    def plot_graph(self,): #  criterion="time"
        """
        Plot the graph using matplotlib, coloring edges based on the mode of transport.
        """
        pos = nx.get_node_attributes(self.route_map, "pos")
        edges = self.route_map.edges(data=True)

        # Define colors for each transport mode
        transport_colors = {
            "Bus": "blue",
            "Train": "green",
            "Bicycle": "red",
            "Walking": "orange",
        }

        # Determine edge colors based on the transport mode
        edge_colors = [transport_colors[data["transport"]] for u, v, data in edges]

        nx.draw(
            self.route_map,
            pos,
            with_labels=True,
            node_size=300,
            node_color="lightblue",
            font_size=10,
            edge_color=edge_colors,
        )

        # Create custom legend handles
        legend_handles = [
            mpatches.Patch(color=color, label=mode)
            for mode, color in transport_colors.items()
        ]

        # Add the legend to the plot
        plt.legend(handles=legend_handles, title="Transport Modes", loc="upper right")

        # Add axis labels and grid
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")
        plt.gca().set_axis_on()
        plt.grid(True)

        plt.show(block=False)

    def format_route(self, route, transport_methods, durations):
        """
        Format the route list into a readable string with transport methods and durations.
        """
        formatted_route = ""
        total_duration = 0
        for i in range(len(route) - 1):
            formatted_route += (
            f"{route[i]} -> {route[i + 1]} by {transport_methods[i]} "
            f"(Duration: {durations[i]:.2f} hours)\n"
            )
            total_duration += durations[i]
        formatted_route += f"Total Duration: {total_duration:.2f} hours"
        return formatted_route
