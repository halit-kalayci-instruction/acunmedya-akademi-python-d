class Vehicle():
    def __init__(self,model):
        self.model = model
    def start(self):
        print(f"{self.model} Araç başlatılıyor..")


class Car(Vehicle):
    def start(self): #method overriding -> Polymorphism
        print(f"{self.model} araba başlatılıyor.")

class Truck(Vehicle):
    def load(self):
        print("Yük yükleniyor..")


car = Car("Hyundai")
car.start()

truck = Truck("Scania")
truck.start()
truck.load()