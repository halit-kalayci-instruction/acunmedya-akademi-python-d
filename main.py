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


# reference,value type
# döngüler
# karar blokları
# fonksiyonlar
print("**** 23.02 *****")
students = [ "Ahmet","Berfin","Alisa","Ayşe" ]
print(students[3]) #indexler 0dan başlar
# built-in
students.append("Fatih")
print(students)
#value type - reference type
a = 10
b = a
b += 50
print(a) #10
print(b) #60
# listelerin reference type olması durumu..
students2 = students
students2.append("Fatma")
print(students) # "Ahmet","Berfin","Alisa","Ayşe","Fatma" -> Referans Tip
print(students2) # "Ahmet","Berfin","Alisa","Ayşe","Fatma"

### karar blokları

# belirli bir şart sağlandığında ilgili satırın execute edilmesi durumudur
age = 18
# indentation
# koddaki scope (kapsam) kavramını uygulamayı
# 1-N satır arası kod çalıştırır.
# ! => Her if bloğu yalnızca 1 adet koşul çalıştırır.
# 
# if 
# if else
# if elif else 
if age >= 18:
    print("Kullanıcı reşit")
if age == 18:
    print("Kullanıcı tam 18 yaşında.")
else: # bu bloktaki hiç bir koşul sağlanmadı.
    print("Kullanıcı reşit değil.")
print("3. print") #main scope -> {}

###

## döngüler
# belirli bir iterasyon ile kodun tekrar execute edilmesi isteniyorsa 
# i => iterasyon,index => her bir iterasyonda o anki veriye verilen takma ad
for i in range(5):
    print(i)
    print("a")
print("****")
for i in range(5,10):
    print(i)
print("*****")
for i in range(5,51,5):
    print(i)
#statik
#dinamik
my_list = ["a","b","c","d"] # veritabanından,dosyadan vs okunduğunu düşünelim..
for obj in my_list:
    print(obj)
text = "Merhaba"
for char in text:
    print(char)
#
#while [koşul] - sağlandığı sürece tekrar ediyor.
#while 10 == 10: # sonsuz döngü - infinite loop -- CTRL + C
    #print("while çalıştı..")
a=0
while a < 10:
    print(a)
    a+=1

user_input = input("Lütfen bir değer giriniz. Çıkmak için q giriniz.")
while user_input != "q":
    print(f"Girdiğiniz değer: {user_input}")
    user_input = input("Lütfen bir değer giriniz. Çıkmak için q giriniz.")  
    

for i in range(10):
    if i == 5:
        continue # iterasyona bu adımı atlayarak devam et.
    print(i)
print("*****")
for i in range(10):
    if i == 5:
        break # iterasyonu bu adımdan itibaren tamamen durdur
    print(i)
##

# fonksiyonlar



#


#----
#oop
#modules
#pip

#---
#yapay zeka için python # numpy,pandas,matplotlib -> kurulumlar