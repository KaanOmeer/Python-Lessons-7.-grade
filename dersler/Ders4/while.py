doymak="hayır"
print("Pizzanız, Afiyet Olsun")
while doymak=="hayır":
    cevap=input("Bir Dilim Daha Pizza İstermisiniz")
    if cevap=="evet":
        continue
    else:
        doymak="evet"