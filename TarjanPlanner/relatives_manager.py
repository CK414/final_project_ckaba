import csv

class RelativesManager:
    def __init__(self, relatives_file):
        self.relatives_file = relatives_file
        self.relatives = self.load_relatives()

    def load_relatives(self):
        # Load relatives from CSV file
        with open(self.relatives_file, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
        
    def get_relatives(self):
        # Return relatives list
        return self.relatives
    
    def list_relatives(self):
        line_width = 65 # Define length of table
        print("--- Relatives List ---".center(line_width))
        print("-" * line_width)
        print("{:<12} {:<15} {:<14} {:<10} {:<10}".format("Relative", "Street Name", "District (Gu)", "Latitude", "Longitude"))
        print("-" * line_width)
        for relative in self.relatives:
            print("{:<12} {:<15} {:<14} {:<10} {:<10}".format(relative['Relative'], relative['Street Name'], relative['District (Gu)'], relative['Latitude'], relative['Longitude']))
        print("-" * line_width)