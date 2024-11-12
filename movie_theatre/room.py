class Room:
    def __init__(self, id, num_seats_premium, num_seats_regular ):   
        self.id = id
        self.num_seats_premium = num_seats_premium
        self.num_seats_regular = num_seats_regular
         

    # def __repr__(self):
    #     return (f"Room: {self.id}, Premium Seats:{self.num_seats_premium}, Regular Seats:{self.num_seats_regular}")