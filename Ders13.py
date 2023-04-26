# break continue pass kullanımı 
harfler =['a','b','c','d']*5
# burada c yi yazdırmasın
for index,harf in enumerate(harfler):
    if index == 2:
        continue
    #veya 
    if(harf=="c"):
        continue
    print(harf)
    
# break dögğden cıkar bitirir