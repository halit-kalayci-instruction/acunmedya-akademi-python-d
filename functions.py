# fonksiyonlar

price = 100
total_price = price + (price * 0.20)
print(total_price)
#

# fonksiyon tanımla
print("*****")
#tanımlama sırasında default parametreler required parametrelerden sonra gelmelidir!
def calculate_tax(price,rate=20): #parametreler # default parameter => rate=20
    total_price = price + (price * (rate/100))
    return total_price

price1 = calculate_tax(100) #print
price2 = calculate_tax(200,10) #üzerine kargo ücreti ekle
price3 = calculate_tax(300) #
price4 = calculate_tax(400) #
price5 = calculate_tax(500) #

print(price1)
print(price2+50)

print("*****")
def sum(a,b):
    return a+b

print(sum(1,2))
print(sum(5,10))

def sum2(*args):
    result = 0
    for number in args:
        result += number
    return result

print(sum2(1,2))
print(sum2(5,3,1,2))
print(sum2(1))

# **kwargs => Araştıralım.

# lambda functions -> Tek satırlık fonksiyonlar için bir syntax alternatifi
topla = lambda a,b: a+b
print(topla(5,10))
#
