def func(dct):
    dct1={}
    for i in dct:
     dct1[i]=dct[i].upper()
    print(dct1)
dct={"Ism": "Ali", "Familya": "Kamolov", "Manzil": "Angren shahri"}
func(dct)