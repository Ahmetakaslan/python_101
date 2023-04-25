# tuple Değiştirilemez liste ve () kullanılır
mytuple=(1,2,5,"ahmet",1) # sonradan eklem çıkarma yapılamaz  => ** immutable ** 
# mesela 
# hata => mytuple[0]=5
ilk_deger=mytuple[0]
print(ilk_deger)

print(mytuple.count(1))  # kaç tane var
print("kaç adet var ",mytuple.count(True))
print("indexi ",mytuple.index("ahmet"))









