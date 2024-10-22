import csv

class TransportManager:
    def __init__(self, transport_file):
        self.transport_file = transport_file
        self.transport = self.load_transport()

    def load_transport(self):
        # Load transport modes from CSV file
        with open(self.transport_file, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
        
    def get_transport(self):
        # Return transport modes list
        return self.transport
    
    def list_transport(self):
        line_width = 73
        print("-" * line_width)
        print("--- Transport List ---".center(line_width))
        print("-" * line_width)
        print("{:<20} {:<15} {:<15} {:<15}".format("Mode of Transport", "Speed (kmh)", "Cost per km", "Transfer Time (min)"))
        print("-" * line_width)
        for transport in self.transport:
            print("{:<20} {:<15} {:<15} {:<15}".format(transport['Mode of Transport'], transport['Speed_kmh'], transport['Cost_per_km'], transport['Transfer_Time_min']))
        print("-" * line_width)