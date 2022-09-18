""" 1. Ornek
 # Kullanicidan kisa kenarlari alın ve hipotenüsü hesaplayin
kisaKenar1 = float(input("1.Kisa Kenari Giriniz : "))
kisaKenar2 = float(input("2.Uzun Kenari Giriniz : "))

hipotenus = ((kisaKenar1**2)+(kisaKenar2**2))**0.5
print("Hipotenus : ",hipotenus)


"""
# Kullanicidan direnc ve akim degerini aliniz ve Voltaj degerini bulunuz
voltaj = float(input("Voltaj degerini giriniz : "))
akim = float(input("Akim degerini giriniz : "))


while True:
    """1.Yol
    if akim == 0:
        akim = float(input("Akim Degeri 0 olamaz!!! Akim degeri giriniz : "))
    else:
        break
    """
    try:
        direnc = voltaj / akim
        break
    except ZeroDivisionError:
        akim = float(input("Akim Degeri 0 olamaz!!! Akim degeri giriniz : "))



print("Direnc : " , direnc) #Farkli data type ları print icinde yazarken , kullanmalısın

# Sozluk yazmak 
kelimeler = {}
for i in range(1,3):
    ing = input("Ingilizce kelimeyi giriniz : ")
    tr = input("Turkce anlamani giriniz : ")
    kelimeler[ing] = tr

print(kelimeler)