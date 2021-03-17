sinav1 = int(input('1. Sınav Notunu Giriniz'))
# noinspection PyInterpreter
sinav2 = int(input('2. Sınav Notunu Giriniz'))
ortalama = (sinav1+sinav2)/2
print("Ortalamanız:",ortalama)
if(ortalama>0) and (ortalama<=45):
    print("Kaldınız")
if (ortalama >=45) and (ortalama<=50):
    print("Geçer")
if (ortalama>=50)and (ortalama<=75):
    print("Orta")
if (ortalama>=75) and (ortalama<=85):
    print("İYİ")
if (ortalama>=85) and (ortalama<=100):
    print("Çok İyi")
if (ortalama == 61):
    print("Ha Gayret Uşağum")













