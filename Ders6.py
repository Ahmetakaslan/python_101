#Liste ve Set

liste = [5,6,8,"ahmet"]
print(liste)
#liste=liste+"ali" # bu yanlış bir liste bir String ile bu şekilde toplanamaz ama
liste=liste+[15]
print(liste)
# veya 
liste2=[5,6,8,5,5]
liste=liste+liste2
print(liste) # bu olur
liste.append("ekle")# sona geldi
liste.insert(0,"yap")#istenilen indise eklem yapılır
print(liste)
print()

liste.pop() # default olarak Son elemanı listeden çıkarır ama index verilebilir
print("Son eleman silindi ",liste)
liste.pop(0)
print("ilk eleman silindi",liste)

#1111111111111111111111   Sort (Sıralama)   11111111111111111111111111
print()
liste3 =[5,1,1,3,69,55,0,15]
liste3.sort()# listeyi sıralar 
print("Sıralanmış liste3 ",liste3)
liste3.reverse()# listeyi tersine çevirir
print("tersine çevir ",liste3)
print("set yapıldı ",set(liste3))# ama liste3 değişmedi sadece o anlık kümeye dönütürdü
print(liste3)
print(type(liste3))
print()
# burada atama yapıldı
liste3=set(liste3)
print("type set oldu  ",type(liste3))


 









