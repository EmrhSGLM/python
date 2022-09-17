# 2 sekilde olusturulur
# sozluk = dict() or sozluk = {}
# key,value seklinde calisir , Java daki HashMap gibi calisir
#Dictionary ler sıralı bir veri degildir
# Dic icindeki value bir veri eklemek istersek, eklemek istedigimiz value nun type na gore islem yapılır

sozluk = {}
print(type(sozluk)) # <class 'dict'>

kisiler = {"Eda" : 28,
           "Emrah" : 34,
           "Osman" : 59,
           "Hakkı" : 50,
           "Kazım": 48,
           "Veli" : 25,
           6 : 71
           }
print(kisiler["Eda"]) # 28
print(kisiler["Emrah"])
print(kisiler[6])# 71

calisanlar = {"Uyeler":["Hakkı","Remzi","Kemal"],
              "Moderatorler":["Pelin","Gamze","Mehmet"],
               "Yoneticiler" : ["Mehmet","Şükrü","Eken"]}

print(calisanlar) # {'Uyeler': ['Hakkı', 'Remzi', 'Kemal'], 'Moderatorler': ['Pelin', 'Gamze', 'Mehmet'], 'Yoneticiler': ['Mehmet', 'Şükrü', 'Eken']}
print(calisanlar["Uyeler"]) # ['Hakkı', 'Remzi', 'Kemal']

calisanlar["S.Uyeler"] = ["Semicenk","Reymen","AllaPulla"]
print(calisanlar) # {'Uyeler': ['Hakkı', 'Remzi', 'Kemal'], 'Moderatorler': ['Pelin', 'Gamze', 'Mehmet'], 'Yoneticiler': ['Mehmet', 'Şükrü', 'Eken'], 'S.Uyeler': ['Semicenk', 'Reymen', 'AllaPulla']}
calisanlar["Uyeler"].append("Rex")
print(calisanlar["Uyeler"])
calisanlar["Moderatorler"].remove("Mehmet") # calisanlar["Moderatorler"].pop()
# pop sonuncu datayi siler
print(calisanlar["Moderatorler"])




#calisanlar.clear() # Tum hepsini siler
#print(calisanlar) {}

#kopyaAl = calisanlar.copy() # kopyasini alir
#print(kopyaAl)

#calisanlar.pop("Uyeler") # pop icine yazila key kaldirir
#print(calisanlar)

#print(calisanlar.values()) # dict_values([['Hakkı', 'Remzi', 'Kemal', 'Rex'], ['Pelin', 'Gamze'], ['Mehmet', 'Şükrü', 'Eken'], ['Semicenk', 'Reymen', 'AllaPulla']])
#tum_Kullanicilar = calisanlar.values()
#for kullanicilar in tum_Kullanicilar:
#    print(kullanicilar)

keys = calisanlar.keys()
#print(keys) # dict_keys(['Uyeler', 'Moderatorler', 'Yoneticiler', 'S.Uyeler'])
#for key in keys:
#    print(key,end=" ") # Uyeler Moderatorler Yoneticiler S.Uyeler

print()

tum_Hersey = calisanlar.items()
#print(tum_Hersey) # dic objesini bir list gibi getirir
for i,j in tum_Hersey:
    print(i,"\n----------------\n",j,"\n")
