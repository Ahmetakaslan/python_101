
'''
veri tipleri 

int       =Integer
float     =Float 
str       =String
bool      =Boolean
list      =List [1,1,2,2,"ahmet","ahmet"] istediğin kadar ekleme yapabilirsin
set       =Set  {1,2,"ahmet"} küme gibi her birinden bir tane bir değer tekrarlanmaz
tup       =(1,2,"ahmet")  elemanlar değişemez  eleman ekelenemez ,silinemez ||| () kullanılır 
dict      ={'isim'="Ahmet"}  

'''
#integer 
deger1=5
#float
deger2=155.5
#string
deger3="Ahmet"
#boolean
deger4=True
#List
deger5=["Ahmet",5,4,True,4]
#set
deger6={1,2,"ahmet"}
print(deger6) #çağırınca içerdekilerini karıştırı ve getirir
#tuple
myTup=(1,2,"ahmet") 
print(myTup[0]) # içerik değiştirilemez eklenemez silinemez sonradan!
#hatalı myTup[0]=5

print(type(deger1))
print(type(deger2))
print(type(deger3))
print(type(deger4))
print(type(deger5))
print(type(deger6))
print(type(myTup))

#mod
print(2%2)
print(5%3)
