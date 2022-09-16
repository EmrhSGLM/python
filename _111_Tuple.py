#a = ()
#b = tuple()

#print(type(a)) # <class 'tuple'>
#print(type(b)) # <class 'tuple'>

#a = (1,2,3,4,5)

#a[2] = 20 # 'tuple' object does not support item assignment
# Tuble halindeki bir objenin hicbir verisi degistirilemez
#print(a)

#yazi = "Emrah SAGLAM"
#yeniYazi = tuple(yazi)
#print(yeniYazi) # ('E', 'm', 'r', 'a', 'h', ' ', 'S', 'A', 'G', 'L', 'A', 'M')

yeni = (10,20,30,"Hakkı","Mehmet",71,"Ramazan",71,71)

print(yeni.index(71)) # 71 degerinin hangi index de oldugunu soyler
print(yeni.index("Ramazan"))
print(yeni.count(71)) # 71 sayisinin kac tane oldugunu soyler
print(yeni.__contains__("Hakkı")) # True
print(yeni.__contains__("Mahmut")) # False

#if yeni.__contains__("Hakkı"): # ikiside ayni gorevi yapar
if "Hakkı" in yeni:
    print("Evet var kardes")

# Degismesini istemediginiz verileri tuble yaparsiniz
