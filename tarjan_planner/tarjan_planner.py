"""
Module containing all functions related to route planning.
"""

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from itertools import permutations
from geopy.distance import geodesic
from .relatives_manager import RelativesManager
from .transport_manager import TransportLinkManager
from .logger import logger, log_execution_time


class TarjanPlanner:
    '''
    Class Containing all functions related to calculating the best route for Tarjan.
    '''
    def __init__(self, relatives_file, transport_file, links_file):
        self.relatives_manager = RelativesManager(relatives_file)
        self.transport_manager = TransportLinkManager(transport_file, links_file)
        self.route_map = nx.Graph()

    def create_graph(self):
        """
        Create a graph with relatives as nodes and edges based on transport modes.
        """
        relatives = self.relatives_manager.get_relatives()
        transport_modes = self.transport_manager.get_transport()
        transport_links = self.transport_manager.get_links()

        # Add nodes for each relative
        for relative in relatives:
            self.route_map.add_node(
                relative["Street Name"],
                pos=(float(relative["Longitude"]), float(relative["Latitude"])),
            )

        # Add edges based on transport links
        for link in transport_links:
            start = link["Start"]
            end = link["End"]
            transport_type = link["Transport Type"]

            relative1 = next((r for r in relatives if r["Street Name"] == start), None)
            relative2 = next((r for r in relatives if r["Street Name"] == end), None)
            
            # Debug: Print matching results
            # if relative1 is None:
            #     print(f"Error: Start node '{start}' not found in relatives")
            # if relative2 is None:
            #     print(f"Error: End node '{end}' not found in relatives")

            if relative1 and relative2:
                distance = geodesic(
                    (float(relative1["Latitude"]), float(relative1["Longitude"])),
                    (float(relative2["Latitude"]), float(relative2["Longitude"])),
                ).km

                transport = next((t for t in transport_modes if t["Mode of Transport"] == transport_type), None)

                if transport:
                    speed = float(transport["Speed_kmh"])
                    cost = float(transport["Cost_per_km"]) * distance
                    travel_time = (
                        distance / speed
                        + float(transport["Transfer_Time_min"]) / 60
                    )
                    self.route_map.add_edge(
                        start,
                        end,
                        distance=distance,
                        travel_time=travel_time,
                        cost=cost,
                        transport=transport_type,
                    )
                    logger.debug(
                        "Edge from %s to %s by %s: time=%.2f, cost=%.2f",
                        start,
                        end,
                        transport_type,
                        travel_time,
                        cost
                    )
                    # Debug: Print edge creation
                    # print(f"Edge created: {start} -> {end} by {transport_type}, time={travel_time}, cost={cost}")

    @log_execution_time
    def find_best_route(self, start_node):
        """
        Find the best route based on travel time using a naive tree search algorithm.
        """
        weight = "travel_time"

        # Generate all possible routes starting from the specified node
        nodes = list(self.route_map.nodes)
        nodes.remove(start_node)
        all_routes = permutations(nodes)

        min_travel_time = float('inf')

        for route in all_routes:
            route = [start_node] + list(route)
            route_data = []
            total_travel_time = 0

            valid_route = True
            for i in range(len(route) - 1):
                edge_data = self.route_map.get_edge_data(route[i], route[i + 1])
                if edge_data is None:
                    # Try the reverse direction
                    edge_data = self.route_map.get_edge_data(route[i + 1], route[i])
                    if edge_data is None:
                        valid_route = False
                        break
                route_data.append({
                    "start": route[i],
                    "end": route[i + 1],
                    "transport": edge_data["transport"],
                    "duration": edge_data[weight],
                    "cost": edge_data["cost"]
                })
                total_travel_time += edge_data[weight]

            if valid_route and total_travel_time < min_travel_time:
                min_travel_time = total_travel_time
                best_route_data = route_data

        # Debug: Print lengths of lists
        # print(f"Path length: {len(best_route)}")
        # print(f"Transport methods length: {len(best_transport_methods)}")
        # print(f"Durations length: {len(best_durations)}")
        # print(f"Costs length: {len(best_costs)}")

        return best_route_data

    def plot_graph(self, best_route_data=None):
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
        
        # Create a figure and axes
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_title("Tarjan's Route Planner")

        # Determine edge colors based on the transport mode
        edge_colors = [transport_colors[data["transport"]] for u, v, data in edges]

        # Separate nodes based on their attributes
        tarjan_nodes = [node for node, data in self.route_map.nodes(data=True) if node == 'Yeoui-daero']
        other_nodes = [node for node in self.route_map.nodes() if node != 'Yeoui-daero']

        # Draw Tarjan's node as a green square
        nx.draw(
            self.route_map,
            pos,
            with_labels=True,
            nodelist=tarjan_nodes,
            edge_color=edge_colors,
            style='dashed',
            node_color='lightgreen',
            node_shape='s',
            node_size=500,
            font_size=6,
            ax=ax
        )

        # Draw other nodes as blue circles
        nx.draw(
            self.route_map,
            pos,
            with_labels=True,
            nodelist=other_nodes,
            edge_color=edge_colors,
            style='dashed',
            node_color='lightblue',
            node_shape='o',
            node_size=500,
            font_size=6,
            ax=ax
        )

        # Create custom legend handles
        transport_handles = [
            mpatches.Patch(color=color, label=mode)
            for mode, color in transport_colors.items()
        ]
        
        # Create custom legend handles for Tarjan's home and residential districts
        location_handles = [
            mpatches.Patch(facecolor='lightgreen', label="Tarjan's Home"),
            mpatches.Patch(facecolor='lightblue', label="Residential Districts")
        ]

        # Create a faint grey line separator
        separator = Line2D([0], [0], color='grey', lw=0.5, linestyle='--')


        # Add the legend to the plot
        legend_handles = transport_handles + [separator] + location_handles
        ax.legend(handles=legend_handles, title="Transport Modes & Locations", loc="upper right")

        # Add axis labels and grid
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.set_axis_on()
        ax.grid(True)
        
        # Highlight the best route if provided
        if best_route_data:
            best_route_edges = [(segment['start'], segment['end']) for segment in best_route_data]
            nx.draw_networkx_edges(
                self.route_map,
                pos,
                edgelist=best_route_edges,
                edge_color=edge_colors,
                arrows=True,
                arrowstyle="-|>",
                width=2,
            )
        
        # Create edge labels
        edge_labels = {
            (u, v): f"{data['distance']:.2f}km"
            for u, v, data in edges
        }

        # Draw edge labels
        nx.draw_networkx_edge_labels(
            self.route_map,
            pos,
            edge_labels=edge_labels,
            font_size=5,
            ax=ax
        )
        
        plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

        plt.show(block=False)
        
    def format_route(self, route_data):
        """
        Format the route for display.
        """
        formatted_route = []
        total_duration = 0
        total_cost = 0
        
        for i, segment in enumerate(route_data):
            formatted_route.append(
                f"{i+1}: {segment['start']} -> {segment['end']} by {segment['transport']} "
                f"(time: {segment['duration'] * 60:.2f} min) (cost: ₩{segment['cost']:.2f})"
            )
            total_duration += segment['duration']
            total_cost += segment['cost']
            
        # Append total duration to the formatted route
        formatted_route.append(f"Total duration: {total_duration:.2f}h [{total_duration*60:.2f} min]")
        formatted_route.append(f"Total cost: KRW {total_cost:.2f}")
        
        return "\n".join(formatted_route)
    