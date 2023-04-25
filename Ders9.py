
# if , else , elif kullanımı 

havaDurumu="Yağışlı"
if havaDurumu=="Yağışlı": # bu doğruysa yap 
    print("Şemsiyeni al")
else: # doğru değilse bunu yap
    print("Şemsiyeye gerek yok")    
    
    
liste=['a','b','c']
hedef="d"
if hedef in liste :
    print("Doğru var ")
else:
    print("Yanlış Yok")
    liste.append(hedef)
    print("Hedef eklendi")
# başka dillerde  && || ve veya manasına gelen 
# and or var 
print()
if((hedef in liste) and (hedef ==liste[len(liste)-1])):
    print("evet listede mevcut ve son eleman")
elif hedef in liste :
    print("Evet lisede var ama son eleman değil")
else: 
    print("listede yok ")    
            
    
    
       
    