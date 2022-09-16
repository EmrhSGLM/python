
facebook_takipceleri = "Osman,Emrah:71,Mehmet,Hakkı"

name = "Emrah"
last_Name = "Saglam"
hakan_Basalangic = facebook_takipceleri.find(name)

print(facebook_takipceleri[hakan_Basalangic:21]) # Hakan'in oldugu yerden basladi 21 index'e kadar yazdirdi

print(facebook_takipceleri[hakan_Basalangic:21:2]) # 2 ser 2 ser atlayarak yazdirir

print(facebook_takipceleri[0:6:2])

print(facebook_takipceleri[-1]) # sondan baslar
print(facebook_takipceleri[::-1]) # ters den yazıyoruz
print(facebook_takipceleri[:3]) # 3. index'e kadar yazdirir
print(facebook_takipceleri[-5])
print(facebook_takipceleri[-5:]) # sondan 5. index'den baslayip sona kadar yazdiriyor
print(len(facebook_takipceleri)) # len uzunlugu hesaplar
print(len(name))

print(name+" "+last_Name)