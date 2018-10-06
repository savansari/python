class car:
    def __init__(self,price, speed, fuel, mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        if price>10000:
            self.tax=15/100
        else:
            self.tax=12/100
        self.display_all()
    def display_all(self):
        print("\nPrice: " ,self.price,"\nSpeed: ",self.speed,"\nFuel: ",self.fuel,"\nMileage: ",self.mileage,"\nTax: ",self.tax)
        
        
car1=car(2000,"35mph","Full","15mpg")
car2=car(2000,"5mph","Not Full","105mpg")
car3=car(2000,"15mph","Kind of Full","15mpg")
car4=car(2000,"25mph","Full","25mpg")
car5=car(2000,"45mph","Empty","25mpg")
car6=car(20000000,"35mph","Empty","15mpg")