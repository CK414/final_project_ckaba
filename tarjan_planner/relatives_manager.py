"""
Module containing all functions related to relatives.
"""

import csv
import os


class RelativesManager:
    """
    Class containing all functions working with relatives data
    """

    def __init__(self, relatives_file):
        self.relatives_file = relatives_file
        self.relatives = self.load_relatives()

    def load_relatives(self):
        """
        Function to load relatives data from file
        """
        # Load relatives from CSV file
        with open(self.relatives_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def get_relatives(self):
        """
        Return relatives list
        """
        return self.relatives

    def list_relatives(self):
        """
        Print relatives table
        """
        line_width = 62  # Define length of table
        print("--- Relatives List ---".center(line_width))
        print("-" * line_width)
        print(
            f"{'Relative':<13}"
            f"{'Street Name':<15}"
            f"{'District (Gu)':<14}"
            f"{'Latitude':<10}"
            f"{'Longitude':<10}"
        )
        print("-" * line_width)
        for relative in self.relatives:
            print(
                f"{relative['Relative']:<13}"
                f"{relative['Street Name']:<15}"
                f"{relative['District (Gu)']:<14}"
                f"{relative['Latitude']:<10}"
                f"{relative['Longitude']:<10}"
            )
        print("-" * line_width)
