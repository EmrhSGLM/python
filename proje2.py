

calisanlar = {"Uyeler":["Hakkı","Remzi","Kemal"],
              "Moderatorler":["Pelin","Gamze","Mehmet"],
               "Yoneticiler" : ["Mehmet","Şükrü","Eken"]}
calisanlar["Moderatorler"].remove("Mehmet") # calisanlar["Moderatorler"].pop()


while True:
    islem = int(input("Yapabileceginiz islemler\n1- Ekle\n2- Kaldir\n3- Cikis\nİsleminizi Seciniz : "))
    if islem == 1:
       key = input("Yetki Seciniz (Uyeler,Moderatorler,Yoneticiler,S.Uyeler) : ")
       if key == "Uyeler":
           name = input("Eklemek istediginiz ismi yaziniz : ")
           calisanlar["Uyeler"].append(name)
           print("Basariyla Eklendi")
           print("Yeni Uyeler Listeniz ",calisanlar["Uyeler"])
       if key == "Moderatorler":
           name = input("Eklemek istediginiz ismi yaziniz : ")
           print("Basariyla Eklendi")
           print("Yeni Moderatorler Listeniz ",calisanlar["Moderatorler"])
           calisanlar["Moderatorler"].append(name)
       if key == "Yoneticiler":
           name = input("Eklemek istediginiz ismi yaziniz : ")
           print("Basariyla Eklendi")
           print("Yeni Yoneticiler Listeniz ",calisanlar["Yoneticiler"])
           calisanlar["Yoneticiler"].append(name)
       if key == "S.Uyeler":
           name = input("Eklemek istediginiz ismi yaziniz : ")
           calisanlar["S.Uyeler"].append(name)
           print("Basariyla Eklendi")
           print("Yeni S.Uyeler Listeniz ",calisanlar["S.Uyeler"])
    elif islem == 2:
       key = input("Yetki Seciniz (Uyeler,Moderatorler,Yoneticiler,S.Uyeler) : ")
       if key == "Uyeler":
           name = input("Silmek istediginiz ismi yaziniz : ")
           calisanlar["Uyeler"].remove(name)
           print("Basariyla Silindi")
           print("Yeni Uyeler Listeniz ",calisanlar["Uyeler"])
       if key == "Moderatorler":
           name = input("Silmek istediginiz ismi yaziniz : ")
           calisanlar["Moderatorler"].remove(name)
           print("Basariyla Silindi")
           print("Yeni Moderatorler Listeniz ",calisanlar["Moderatorler"])
       if key == "Yoneticiler":
           name = input("Silmek istediginiz ismi yaziniz : ")
           calisanlar["Yoneticiler"].remove(name)
           print("Basariyla Silindi")
           print("Yeni Yoneticiler Listeniz ",calisanlar["Yoneticiler"])
       if key == "S.Uyeler":
           name = input("Silmek istediginiz ismi yaziniz : ")
           calisanlar["S.Uyeler"].remove(name)
           print("Basariyla Silindi")
           print("Yeni S.Uyeler Listeniz ",calisanlar["S.Uyeler"])
    elif islem == 3:
        print("Gule Gule")
        break
    else :
        print("Yanlıs giris yaptiniz")