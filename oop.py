# object oriented programming
# nesne yönelimli programlama

class Car():
    def __init__(self, model):
        self.__model = model
        print("Yeni car üretildi.")

    def start(self):
        print(f"{self.__model} araba başlatılıyor..")

    def increase_speed(self, amount):
        print(f"Hız şu kadar artırılıyor: {amount}")
    
    # getter
    def get_model(self):
        return self.__model
    # setter
    def set_model(self,model):
        if len(model) < 3:
            print("Marka ismi 3 haneden küçük olamaz")
            return
        self.__model = model

car = Car("Hyundai") # instance
car.set_model("a")
car.start() 
car.increase_speed(50)

car1 = Car("Honda") # ilgili classın yapıcı methodunu çağırır (constructor)
car1.start()