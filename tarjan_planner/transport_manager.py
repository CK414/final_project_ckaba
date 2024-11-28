"""
Module containing all functions related to relatives.
"""

import csv


class TransportManager:
    """
    Class containing all functions working with transport data
    """

    def __init__(self, transport_file):
        self.transport_file = transport_file
        self.transport = self.load_transport()

    def load_transport(self):
        """
        Function to load transport data from file
        """
        # Load transport modes from CSV file
        with open(self.transport_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def get_transport(self):
        """
        Return transport modes list
        """
        return self.transport

    def get_transport_by_mode(self, mode):
        """
        Return the transport mode details based on the transport mode name.
        """
        for transport in self.transport:
            if transport["Mode of Transport"] == mode:
                return transport
        raise ValueError(f"Transport mode '{mode}' not found")

    def list_transport(self):
        """
        Print transport modes table
        """
        line_width = 68
        print("-" * line_width)
        print("--- Transport List ---".center(line_width))
        print("-" * line_width)
        print(
            f"{'Mode of Transport':<20}"
            f"{'Speed (kmh)':<14}"
            f"{'Cost per km':<14}"
            f"{'Transfer Time (min)':<14}"
        )
        print("-" * line_width)
        for transport in self.transport:
            print(
                f"{transport['Mode of Transport']:<20} "
                f"{transport['Speed_kmh']:<13} "
                f"{transport['Cost_per_km']:<13} "
                f"{transport['Transfer_Time_min']:<14}"
            )
        print("-" * line_width)
        
class TransportLinkManager(TransportManager):
    """
    Class containing all functions working with transport links data
    """

    def __init__(self, transport_file, links_file):
        super().__init__(transport_file)
        self.links_file = links_file
        self.links = self.load_links()

    def load_links(self):
        """
        Function to load transport links from file
        """
        # Load transport links from CSV file
        with open(self.links_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def get_links(self):
        """
        Return transport links list
        """
        return self.links

    def list_links(self):
        """
        Print transport routes table
        """
        line_width = 50
        print("-" * line_width)
        print("--- Transport Routes ---".center(line_width))
        print("-" * line_width)
        print(
            f"{'Transport Type':<16}"
            f"{'Start':<17}"
            f"{'End':<17}"
        )
        print("-" * line_width)
        for link in self.links:
            print(
                f"{link['Transport Type']:<15} "
                f"{link['Start']:<16} "
                f"{link['End']:<16}"
            )
        print("-" * line_width)
