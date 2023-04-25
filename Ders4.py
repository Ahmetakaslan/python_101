
# String ve Char kullanımı

deger1="Fare"
print(deger1)
'''
mesela 
F  a  r   e
0  1  2   3
0 -3 -2 -1 
'''
print(deger1[0]) #F
print(deger1[-1]) #E
print(deger1[3])  #E

print(deger1[:]) # hepsi
print(deger1[:1]) # indis 1' kadar dahil değil
print(deger1[1:]) # indis 1 den başla
print("----")
print(deger1[1:3])
print(deger1[0:3:2]) # iki atla 0 dan başla 3 kadar 


#      ************       length   ************ 
print(len(deger1)) #uzunluk
print(deger1*5) # kere tekrar et
print(deger1.upper())
print(deger1.lower())
print(deger1.split()) # bu kelimeyi boşluğa göre ayırıyor 
print(deger1.split("a")) # a yı almıyor
deger2="Ali top aldı. Eve git   ti"
print(deger2.split("i"))
print(deger2.split("i",1)) # ikincisi indeks ve kaç parçaya bölünmesini istiyor


