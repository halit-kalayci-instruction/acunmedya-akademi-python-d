# pythonda built-in bulunan modüller
# local modüller (kendi proje dosyalarım)
# 3. taraf kütüphaneler
# import math
from math import sqrt as karekok, pi
from inheritance import Car
import requests
# alias -> takma ad

print(karekok(25))
print(pi)

c1 = Car("Hyundai")
c1.start()

response = requests.get("https://google.com")
print(response.status_code)