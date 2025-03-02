# object oriented programming
# nesne yönelimli programlama

class Car():
    model = ""

    def start(self):
        model = "Toyota"
        print(f"{self.model} araba başlatılıyor..")

    def increase_speed(self, amount):
        print(f"Hız şu kadar artırılıyor: {amount}")

car = Car()   # instance
car.model = "Hyundai"
car.start() 
car.increase_speed(50)
