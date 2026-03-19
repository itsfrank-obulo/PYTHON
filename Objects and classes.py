#the class
class Car:
    brand= "Toyota Fielder"
    def drive(self):
        print(f"the {self.brand} is now moving!")
        
#the object
my_car=Car()
print(my_car.brand)
my_car.drive()
        