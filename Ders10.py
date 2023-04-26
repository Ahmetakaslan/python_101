# Loop (Döngüler) While For
siparisler=["Elma","Armut","Kivi"]
adet=0
for meyveler in siparisler:
    print()
    adet+=1
    print(f"{adet}",meyveler)
    print()

myTub=(1,2,3)
for sayi in myTub:
    print(sayi)
print("******")

liste=[[1,2],[3,4]]   # listenin içindeki eleman sayısına değil eleman çiftlerinin sayısına göre x,y yi artıtıp azaltırız 
for x,y in liste:
    print(x)
    
    
#/**////////////////////

kullanici={
    'ad':'Ali',
    'soyad':'Dağ'
}    
print(kullanici.items())
for x,y in kullanici.items():
    print(x,y)
   
    
    

    
    
            
    

    