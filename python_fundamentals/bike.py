class bike:
    def __init__(self, price,max_speed):
        self.price=price
        self.max_speed=max_speed
        self.miles=0
    def displayInfo(self):
        print(f"Max-Speed: {self.max_speed} , Miles: {self.miles} , Price: {self.price}")
    def ride(self):
        self.miles+=10
        print("Riding...")
        return self
    def reverse(self):
        self.miles-=5
        print("Revering...")
        return self

bike1=bike(100,"25mph")
bike1.ride().ride().ride().reverse().displayInfo()

bike2=bike(100,"25mph")
bike2.ride().ride().reverse().reverse().displayInfo()

bike3=bike(100,"25mph")
bike3.reverse().reverse().reverse().displayInfo()