import CarClass as c

def main():

    car = c.Car('2010', 'Chevy Malibu')

    i=0

    while i <= 4:
        car.accelerate()
        car.get_speed()
        i+=1

    i = 0

    while i <= 4:
        car.brake()
        car.get_speed()
        i+=1

main()