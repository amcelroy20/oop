import random

class Insect:

    def __init__(self):
        self.legs = 4
        self.wings = 2
        self.flight_dist = 0

    def flight(self):
        self.flight_dist = random.randint(1,10)

    def get_flightdist(self):
        return self.flight_dist
