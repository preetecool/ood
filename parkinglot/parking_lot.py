from parking_space import ParkingSpace
from vehicle import Vehicle
from ticket import Ticket

class ParkingLot:
    def __init__(self, num_regular, num_handicap, num_compact):
        self.spaces = []
        self.create_spaces(num_regular, "Regular")
        self.create_spaces(num_handicap, "Handicap")
        self.create_spaces(num_compact, "Compact")
    
    def create_spaces(self, num_spaces, size):
        start_id = len(self.spaces) + 1
        for i in range(num_spaces):
            self.spaces.append(ParkingSpace(f"{size}-{start_id + i}", size))
    
    def find_available_space(self, vehicle):
        for space in self.spaces:
            if not space.is_occupied and self.match_vehicle_size(space, vehicle):
                return space
        return None

    
    def match_vehicle_size(self, space, vehicle):
        if vehicle.size == "Handicap" and space.size == "Handicap":
            return True
        elif vehicle.size == "Compact" and space.size in ["Compact", "Regular"]:
            return True
        elif vehicle.size == "Regular" and space.size == "Regular":
            return True
        return False

    def park(self, vehicle):
        space = self.find_available_space(vehicle)
        if not vehicle:
            raise ValueError("Cannot park a null vehicle")
        if space:
            space.park(vehicle)
            return Ticket(f"T-{vehicle.license_plate}", vehicle, space)
        else:
            print("No suitable parking space available.")
            return None
    
    def unpark(self, ticket):
        ticket.parking_space.unpark()



