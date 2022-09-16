yazi = "ASDG"

print(*yazi) # print("A",S","D","G")
print(*yazi,sep=".")

def sayilariTopla(*degerler):
    toplam = 0
    for deger in degerler:
        toplam += deger
    return toplam
print(sayilariTopla(1,2,3,4,5))

sayilar = [x for x in range(1,1001)]

print(sayilar)
print(type(sayilar))

print(sayilariTopla(*sayilar)) # 1 den 1000 e kadar olan sayilarin toplami

def sayilariTopla1(sayilar):
    for sayi in range(1,sayilar):
        print(sayi,end="")
sayilariTopla1(101)
