# entrypoint dosyası => main,index,program

# programlama nedir

# değişkenler - variables
age = 25 # int,integer => Tam sayı
print(age)

age = 30 # int,integer
print(age)
#

name = "Halit" #str,string
print(name)
print( type(name) )


name = 30
print(name)
print( type(name) )
# değişkenler tipi

# python type-safe değildir.

# operatörler
#aritmetik (matematiksel) operatör
# float,double,decimal
print(1+1)
print(10-5)
print(5*10)
print(26/5)
print(25//5)
print(29//5)
print(100%3) # mod
print(5**3) # üs alma
#

#atama operatörleri
a = 1
a += 5 # a'nın değerini +5 yap demek => a = a + 5
a -= 3
a *= 2 # a = a * 2
a //= 1
print(a)
#

is_valid = True  #bool, boolean
# karşılaştırma operatörleri
print(1 == 1) # == sağ ve sol eşitse True değilse False
print(1 == 2)
print(3 != 3)

print(10 > 5)
print(10 >= 5)

print(5 < 10)
print(5 <= 10)
# ASCII değerine göre
print("halit" == "halit")

print("car" > "bus")

# mantıksal operatörler -> and, or, not
print("*****")
print( 1==1 and 10 > 5 ) # ve => true&true -> true, false
print( 1==2 and 10 > 5)

print( 1==1 or 10 > 5 ) # veya => false&false => false, true
print( 1==2 or 10 > 5)
print( 1==2 or 10 < 5 and 1==1 )
#

print(  1==1 and 5<3 or 10==10 and 5>=6 )
# işlem önceliği => soldan başlar parantez,and,or diye gider.
print( ( 1==1 and 2>5 ) or 6>=6 and ( 10>5 or 5 == 5 ) )

print(not 1==1)