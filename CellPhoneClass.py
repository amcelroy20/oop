class CellPhone:

    def __init__(self):
        self.__manufact = "Apple"
        self.__model = "iPhone 15"
        self.__retail_price = 1099

    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price
    
    def get_manufact(self):
        return self.__manufact
    
    def get_model(self):
        return self.__model
    
    def get_retail_price(self):
        return self.__retail_price