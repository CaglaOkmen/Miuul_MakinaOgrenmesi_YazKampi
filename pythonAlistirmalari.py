# Miuul Python Alıştırmaları

# Gorev 1: Verilen değerlerin veri yapılarını inceleyiniz.

x = 8
type(x) # int

y = 3.2
type(y) # float

z = 8j + 18
type(z) # complex

a = "Hello World!"
type(a) # str

b = True
type(b) # bool

c = 23 < 22
type(c) # bool

l = [1, 2, 3, 4]
type(l) # list

d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
type(d) # dict

t = ("Machine Learning", "Data Science")
type(t) # tuple

s = {"Python", "Machine Learning", "Data Science"}
type(s) # set

# Görev 2: Verilen string ifadenin tüm
# harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz,
# kelime kelime ayırınız.

text = "The goal is to turn data into information, and information into insight."
text.replace(".", " ").replace(",", " ").upper().split()

#Görev 3:Verilen listeye aşağıdaki adımları uygulayınız.
lst =["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
# Adım 1: Verilen listenin eleman sayısına bakınız.
# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
# Adım 4: Sekizinci indeksteki elemanı siliniz.
# Adım 5: Yeni bir eleman ekleyiniz.
# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

len(lst) # 11
lst[0:11:10]  # ['D', 'E']  -10 adım atlayarak
lst[0:4] # ['D', 'A', 'T', 'A']
lst.pop(8)
lst.append("C")
lst.insert(8, "N")

# Görev 4:  Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
dict = {'Christian': ["America",18],
        'Daisy': ["England",12],
        'Antonio': ["Spain",22],
        'Dante': ["Italy",25]}
# Adım1: Key değerlerine erişiniz.
# Adım2: Value'lara erişiniz.
# Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
# Adım4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
# Adım5: Antonio'yu dictionary'den siliniz.

dict.keys()
dict.values()
dict['Daisy'] = ["England",13]
dict.update({'Ahmet': ["Turkey",24]})
dict.pop('Antonio')

# Görev 5:Argüman olarak bir liste alan, listenin içerisindeki
# tek ve çift sayıları ayrı listelere atayan ve
# bu listeleri return eden fonksiyon yazınız.
l = [2,13,18,93,22]

def func(x):
    cift_list = []
    tek_list = []
    for i in x:
        if i % 2 == 0:
            cift_list.append(i)
        else:
            tek_list.append(i)
    return f"cift: {cift_list} tek:  {tek_list}"
func(l)

# Görev 6: Aşağıda verilen listede mühendislik ve
# tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını
# temsil ederken son üç öğrencide tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]

for index, ogrenci in enumerate(ogrenciler, 1):
    if index < 4:
        print("Mühendislik fakültesi ", index, ". ogrenci: ", ogrenci)
    else:
        print("Tip fakultesi ", index-3, ". ogrenci: ", ogrenci)

# Görev 7: Aşağıda 3 adet liste verilmiştir.
# Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır.
# Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]
# list(zip(ders_kodu,kredi,kontenjan))
for kod, kredi, kont in zip(ders_kodu, kredi, kontenjan):
    print(f"Kredisi {kredi} olan {kod} kodlu dersin kontenjanı {kontenjan} kişidir.")

# Görev 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise
# ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden
# farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "Lambda", "python", "miuul"])

kume1.issuperset(kume2) # False
kume2.difference(kume1)
# kume2.intersection(kume1)
