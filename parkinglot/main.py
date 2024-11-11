from parking_lot import ParkingLot
from vehicle import Vehicle

def main():
    parking_lot = ParkingLot(num_regular =100, num_handicap=10, num_compact=10 )

    car = Vehicle("CAR-001", "Regular")
    bike = Vehicle("BIKE-001", "Compact")
    handicap_van = Vehicle("VAN-999", "Handicap")
    
    ticket1 = parking_lot.park(car)
    ticket2 = parking_lot.park(bike)
    ticket3 = parking_lot.park(handicap_van)

    parking_lot.unpark(ticket1)



if __name__ == "__main__":
    main()

