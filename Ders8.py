# Dictionary
myDictionary = {
    "adı": "Ahmet",
    "yaş": 20
}
print(myDictionary)

secDictionary = {
    "isim": "Ahmet",
    "Soyisim": "Akaslan",
    "Şehirler": {
        "Yaşadığı il": "Mardin",
        "Doğduğu il": "Mardin",
    }, }
print(secDictionary)
print(secDictionary["isim"]) # değeri alır

print()
print("yaşadığı il =>",secDictionary["Şehirler"]["Yaşadığı il"])
print("Doğduğu il =>",secDictionary["Şehirler"]["Doğduğu il"])
# bunların kullanımının farklı yolu var okunuşu da arttırır

print(secDictionary.get("Şehirler").get("Yaşadığı il"))
print(secDictionary.keys())# keyleri alır
print(secDictionary.values())# value leri alır
print(secDictionary.items())# her bir değeri verir 








