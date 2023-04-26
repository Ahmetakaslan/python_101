print("""       Hesap Makinesi      """)

sayi1 = float(input("birinci sayiyi giriniz :"))
sayi2 = float(input("ikinci sayiyi giriniz  :"))
print(f"""
      Toplamı:{abs(sayi1+sayi2)} 
      farkı:{abs(sayi1-sayi2)} 
      çarpımı:{abs(sayi1*sayi2)} 
      bölümü:{abs(sayi1/sayi2)} 
      
      """)
# ek olarak bir bilgi sep ile ayrılanın arasına istediklerini ekleyebilirsin
#* ile de ayırabilirsin
string="ahmet"
print(*string,sep=" / ")

