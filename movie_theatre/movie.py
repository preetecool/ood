class Movie:
    def __init__(self, title, showtimes):
        self.title =title
        self.showtimes = {} #dayofweek: [times]