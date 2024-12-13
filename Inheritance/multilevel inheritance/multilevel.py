class car():
    def __init__(self,speed):
        self.speed=speed
    def carinfo(self):
        print("the car speed is ",self.speed)

class brand(car):
    def __init__(self,compony,speed):
        self.compony=compony
        super().__init__(speed)
    def brandinfo(self):
        self.carinfo()
        print("brand name is",self.compony)
        

class price(brand):
    def __init__(self,rate,compony,speed):
        self.rate=rate
        super().__init__(compony,speed)
    def price(self):
        self.brandinfo()
        print("The rate if the car is",self.rate)

obj=price("25000","Tata","100 km/hr")
obj.price()