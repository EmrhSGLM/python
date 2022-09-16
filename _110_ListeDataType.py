
#list() ya da [] bu sekilde list objesi olusturulabilir

a = list()
b = []

print(type(a))
print(type(b))

ogrenciler = ["Amine","Eda","Emrah","Osman","Kerem","Hakkı","Hasan","Kemal","Ayşe","Veli"]
print(ogrenciler[2]) # Emrah

for ogrenci in ogrenciler:
    print(ogrenci,end=" ") # Amine Eda Emrah Osman
print()
#ogrenciler.remove("Emrah")
print(len(ogrenciler))
print(ogrenciler)
print(ogrenciler[0:2]) # 0. index den 2. index'e kadar olan elemanları consola yazar
basariligrenciler = ogrenciler[0:3]
print(type(ogrenciler))
print(type(basariligrenciler))

print(ogrenciler[5:1:-1]) # 5. indexden baslayip 1. index'e kadar yazacak ters den yazacak
#['Hakkı', 'Kerem', 'Osman', 'Emrah']
ogrenciler[4] = "Kerime"
print(ogrenciler)

isim = "Serkan Olmez"
isim = list(isim)
isim[0] = "C"
print("".join(isim)) # listi string'e cevirir

ogrenciler2 = ["Musa","Zeynep","Leyla"]
ogrenciler = ogrenciler + ogrenciler2 # listeler bu sek,lde birbirine eklenebiliyor
print(ogrenciler)

liste= [1,2,3]
liste = liste*3
print(liste)
liste.append("Emrah")
print(liste)
cikarilan = liste.pop() # parametre girilmez ise en sondaki elemanı cıkarır
print(liste)
print(cikarilan)
liste2=[56,54,89,25,65,800,2365,369,58,1,256,4]
liste2.sort()
print(liste2)
liste2.sort(reverse=True) # listeyi buyukten kucuge sıralar
print(liste2)

kullanicilar = ["XYZ71","ABC06","KARA54"]
sifre = ["12345","56987","85236"]

users = [kullanicilar,sifre] # ic ice liste or array

print(users[0][0],users[1][0])