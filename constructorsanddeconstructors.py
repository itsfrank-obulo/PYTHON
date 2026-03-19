class Phone:
    #the constructor
    def __init__(self, brand, model, price):
        self.brand= brand
        self.model= model
        self.price= price
        
        print(f"my phone is a {self.brand} {self.model} and it costs Ksh {self.price}")
        
        #the decontructor
    def __del__(self):
        print(f"the {self.brand} {self.model} is out of stock!")
        
        #constructor triggers
my_phone= Phone("Samsung", "Galaxy S21", 50000)

#deconstructor triggers
del my_phone
