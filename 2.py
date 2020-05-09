

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def coast(self):
        return self.speed * 100
    
    def update_model(self):
        self.speed = self.speed + 10
    
    def info(self):
        print(self.name)
        print(self.speed * 100)
        print(self.speed)

class Speed_Car(Car):
    def coast(self):
        return self.speed * 250
    
    def update_model(self):
        self.speed = self.speed + 15

car = Car("Porche",240)
speed_car = Speed_Car("AE-12",360)
car.info()
speed_car.info()
car.update_model()
speed_car.update_model()
car.info()
speed_car.info()

