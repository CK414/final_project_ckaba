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

    def list_transport(self):
        """
        Print transport modes list
        """
        line_width = 73
        print("-" * line_width)
        print("--- Transport List ---".center(line_width))
        print("-" * line_width)
        print(
            f"{'Mode of Transport':<20}"
            f"{'Speed (kmh)':<15}"
            f"{'Cost per km':<15}"
            f"{'Transfer Time (min)':<15}"
        )
        print("-" * line_width)
        for transport in self.transport:
            print(
                f"{transport['Mode of Transport']:<20} "
                f"{transport['Speed_kmh']:<15} "
                f"{transport['Cost_per_km']:<15} "
                f"{transport['Transfer_Time_min']:<15}"
            )
        print("-" * line_width)