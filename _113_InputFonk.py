#Input Fonksiyonu
# disardan gelen veriye gore islem yapmamizi sagliyor
# bu da islemin dinamik olmasini sagliyor
# input girilen degeri her zaman string olarak kabul ediyor

def kareAl(a):
    return a**2 # a*a ayni islemi yapar

sayi = int(input("Please enter a number : "))
print(kareAl(sayi))

print("""
*** HESAP MAKİNESİ
""")
sayi1 = int(input("Birinci sayiyi giriniz : "))
sayi2 = int(input("İkinci sayiyi giriniz : "))

print("""
Toplam : {}
Fark : {}
Carpim : {}
Bolum : {}
""".format(sayi1+sayi2,sayi1-sayi2,sayi1*sayi2,sayi1/sayi2))