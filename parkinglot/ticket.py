class Ticket:
    def __init__(self, ticket_id, vehicle, parking_space):
       self.ticket_id = ticket_id
       self.vehicle = vehicle
       self.parking_space = parking_space

    def __repr__(self):
        return (f"Ticket({self.ticket_id}, {self.vehicle.license_plate}, {self.parking_space.space_id})")
