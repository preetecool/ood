from typing import List, Dict
from datetime import datetime, timedelta
from movie import Movie
from room import Room
from showtime import Showtime

class Theatre:
    def __init__(self, id, address, name):
        self.id = id
        self.address = address
        self.name = name
        self.curr_movies: Dict[str, Movie] = {}
        self.rooms:Dict[str, Room] = {}
        self.showtimes:Dict[str, List[Showtime]] = {}
    
    def add_movie(self, movie: Movie):
        if movie.id in self.curr_movies:
            raise ValueError(f"Movie with ID {movie.id} already exists in theatre")
        self.curr_movies[movie.id] = movie
        self.showtimes[movie.id] = []
        return True

    
    def remove_movie(self, movies):
        for movie in movies:
            if movie in self.curr_movies:
                self.curr_movies.remove(movie)
                
    def add_room(self, room):
        if room.id in self.rooms: 
            raise ValueError(f"Room with ID {room.id} already exists in theatre")
        rooms[room.id] = room
        return True
    
    def schedule_showtime(self, movie_id:str, room_id:str, start_time:datetime, price_multiplier: float = 1.0):
        if movie_id not in self.curr_movies:
            raise ValueError("f Movie ID{movie_id} does not exist.")
        if room_id not in self.rooms:
            raise ValueError("f Room ID {room_id} does not exist.")

        for movie, showtimes in  self.showtimes.items():
            for showtime in showtimes:
                if(showtime.room_id == room_id and self._times_overlap(showtime.start_time,
                                                                       self.curr_movies[movie].duration, 
                                                                       start_time, 
                                                                       self.curr_movies[movie_id].duration)):
                    return False
        new_showtime = Showtime(movie_id = movie_id, 
                                room_id = room_id,
                                start_time = start_time,
                                price_multiplier = price_multiplier)
        self.showtimes[movie_id].append(new_showtime)
        return True
    
    def get_available_showtimes(self, movie_id:str, date:datetime):
        if movie_id not in self.showtimes:
            raise ValueError(f"Movie with ID{movie_id} is not currently playing")

        return [
            showtime for showtime in self.showtimes[movie_id]
            if showtime.start_time.date() == date.date()
            and showtime.has_available_seats()
        ]
    
    def get_room_capacity(self, room_id:str):
        
        if room_id not in self.rooms:
            raise ValueError(f"Room ID:{room_id} does not exist")
        
        room = self.rooms[room_id]
        return {
            'total_seats':room.get_total_seats(),
            'available_premium': room.get_available_premium_seats(),
            'available_regular': room.get_available_regular_seats()
        }
        
    @staticmethod
    def _times_overlap(start1: datetime, duration1:int, start2:datetime, duration2:int):
        end1 = start1 + timedelta(minutes=duration1 + 30) #adding 30 minutes for cleanup
        end2 = start2 + timedelta(minutes=duration2 + 30) 
        return start1 < end2 and start2 < end1
