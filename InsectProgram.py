import InsectClass as c


def main():

    mosquito = c.Insect(2,4,'Mosquito')
    housefly = c.Insect(2,4,'Housefly')

    print("Let's see how far they flew...")

    mosquito.flight()
    housefly.flight()

    print(f"The mosquito flew: {mosquito.get_flightdist()} miles")
    print(f"The Housefly flew: {housefly.get_flightdist()} miles")


main()