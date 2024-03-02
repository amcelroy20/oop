class RetailItem:

    def __init__(self, name):
        self.__name = name
        
    def set_values(self):
        print(f'Please describe {self.__name}. ')
        self.__desc = input()
        print(f'How many units of {self.__name} are in stock? ')
        self.__stock = input()
        print(f'How much does one unit of {self.__name} cost? ')
        self.__price = input()

    def print_values(self):
        print(self.__name)
        print(f'Description: {self.__desc}')
        print(f'Units in Inventory: {self.__stock}')
        print(f'Price: {self.__price}')