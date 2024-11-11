class ParkingSpace:
    def __init__(self, space_id, size):
        self.space_id = space_id
        self.size = size
        self.is_occupied = False

    def park(self):
        if self.is_occupied:
            raise Exception("Space is occupied.")
        self.is_occupied = True

    
    def unpark(self):
        if not self.is_occupied:
            raise Exception("Space is already empty.")
        self.is_occupied = False

