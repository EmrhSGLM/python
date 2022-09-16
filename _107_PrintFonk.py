
def faktoriyelAl(sayi):
    faktoriyel = 1
    for i in range(1, sayi+1):
        faktoriyel = faktoriyel * i

    return faktoriyel
print(faktoriyelAl(5))

def hesapla(*sayilar,islem):
    if islem == "+":
        sonuc = 0
        for i in sayilar:
            sonuc += i
    else:
        sonuc = 1
        for i in sayilar:
            sonuc *= i
    return sonuc
print(hesapla(1,2,3,4,5,6,islem="*"))

a = 71
b = "Emrah"
print(a,b)
print(a,b,sep=" X ") # 71 X Emrah Saglam parametreler arasına sep parametresinin value sunu koyar

def islem(sayi, yapi="+"):
    if yapi == "+":
        return sayi+sayi
    else:
        return sayi*sayi
print(islem(5)) # yapi'yi default olarak method icerisindeki parametre gibi algılayacak
print(islem(5, yapi="*"))

print(b,end="") # default olarak end parametresi \n dir
print(b)

# * parametresi
print(*b) #E m r a h : indexdeki elemanları tek tek yazar

ad = "Emrah"
soyad = "Saglam"
print("Merhaba Sayin {} {}, hosgeldiniz".format(ad,soyad)) # {} : stringlere ait bir ozelliktir
print("Merhaba Sayin %s %s, hosgeldiniz" % (ad,soyad))
