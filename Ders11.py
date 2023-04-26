# While kullanımı
x=1
while x<10:
    print("{} değeri 10 dan küçüktür".format(x))
    x+=1
# veya 

print("****************************************************")

x=0
while x<10:
    print(f"{x} değeri 10 dan küçüktür")
    x+=1   

print("\n")

# birede while else kullanılabilir
b=12
while b>0:
    print(f"{b} 0' dan büyük")
    b-=1
else:print(f"{b} 0 dan büyük değil")
'''
While ile Faktöriyel hesabı 
5!=5*4*3*2*1
4!=4*3*2*1
'''
x=int(input("Faktöriyeli alınacak tam sayıyı giriniz\n"))
bb=x
faktoriyel=1
while x>1:
    faktoriyel*=x
    x-=1
print(f"{bb} faktöriyel =",faktoriyel)

    
    

