# Kullanımı kolaylaşıracak yapılar 
'''
range()
enumerate()
zip()
'''


#*************************  range()  *********************
#*********


range(0,10)
print(type(range(0,10)))
# listelerdeki kullanım kolaylığı * kulllanılması gerek
listem=[range(0,10)]
print(listem)
listem=[*range(0,10)]
print(listem)
#*************************
print("\n")
#range() itterable bir değer yani yinelenebilir
for sayi in range(10):
    print(sayi)

#*************************  enumerate()  ********************* 
#*************************  enumerate()  ********************* 

  
# indisi keendisi veriyor listelerde mesela
listem=["a","b","c","d","f"]
for a in listem:
    print(a)
print("******** Fark indisi senin yerine vermesi *************")
    
for a in enumerate(listem):
    print(a)    
    
# buda yapılabilir sadece indexleri verebilir
for index,a in enumerate(listem):
    print(index)    
    
    
#*************************  zip()  ********************* 
#*************************  zip()  ********************* 

# zip iki listeyi birbirine göre düzenler mesela

listem=["Ahmet","Ali","Berk","Can","Yasin"]
siralama=range(6)
for x in zip(listem,siralama):
    print(x)
'''
Sonuç 
('Ahmet', 0)
('Ali', 1)
('Berk', 2)
('Can', 3)
('Yasin', 4)
'''    
# veya 
for x,y in zip(listem,siralama):
    print(x)# bu listem'dekileri 
    print(y)# bu ise siralama'daikileri
    


    
    



