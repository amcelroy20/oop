class Car:

    def __init__(self, year, make):
        self.__year = year
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5 

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        print(f'Current speed is: {self.__speed}')
