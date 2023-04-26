# pythonda * kullanımı
isim="Ahmet"
print(*isim)
# ayrı yetten bu da yapılabilir
print(*isim , sep=" / ") # buda ayrılanın arasına eklem yapar

def topla(*sayi:int):
    toplam=0
    for x in sayi:
        toplam+=x
    print(toplam)     
topla(1,2,3,4,5,6,7,8,9)
