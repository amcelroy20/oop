import random

class Insect:

    def __init__(self,w,l,n):
        self.legs = l
        self.wings = w
        self.flight_dist = 0
        self.name = n

    def flight(self):
        self.flight_dist = random.randint(1,10)

    def get_flightdist(self):
        return self.flight_dist
