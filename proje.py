#import skomutlar
sayac = 0;
komut = input("Yapacagınız islemler\n1-Kitap Ekle\n2-Kitap Sil\n3-Cikis\nYapacaginiz islemi giriniz => ")
def anaMenu():
    komut = input("Yapacagınız islemler\n1-Kitap Ekle\n2-Kitap Sil\n3-Cikis\nYapacaginiz islemi giriniz => ")




if int(komut) == 1:
    dosya = open("kitaplar.txt","w")
    kitapIsmi = input("Kitap ismini giriniz => ")
    dosya.write(kitapIsmi.format())
    dosya.close()
    anaMenu()

if int(komut) == 2:
    with open("kitaplar.txt","a") as f:
        lines = f.readlines()
    kitapIsmi = input("Kitap ismini giriniz => ")
    with open("kitaplar.txt", "a") as f:
        for line in lines:
           if line.strip("\n") != kitapIsmi :
               f.write(line)
    anaMenu()
