# Phyton String Veri Tipi ve Özellikleri

# python'da "" ve '' bu sekilde string verileri yazabilirsiniz

text = "Emrah SAGLAM"

def tekrarliYazdir(tekrar_Sayisi , yazilacak_Text):
    for i in range(tekrar_Sayisi):
        pass #print(yazilacak_Text)

tekrarliYazdir(10,text)

yazi = """
<html>
<head></head>
<body><p>Selam</p></body>
</html>
"""
#print(yazi.replace("p","b"))

yeniYazi = []
for harf in yazi:
    if harf == "p":
        yeniYazi.append("b")
    else:
        yeniYazi.append(harf)

#print("".join(yeniYazi))

print(text[0]) # 0. index deki eleman
print(text[0:5]) # 0. elemandan 5.elemana kadar alır

facebook_takipceleri = "Osman,Hakan:71,Mehmet,Hakkı"

isim = "Hakan"
isim_uzunluk = len(isim)

#print(facebook_takipceleri[facebook_takipceleri.find("Hakan")+isim_uzunluk:facebook_takipceleri.find("Hakan")+isim_uzunluk+3])


