import random
secenekler = ["Taş","Kağıt","Makas"]
bilgisayar = random.choice(secenekler)
kullanici = input("Taş mı Kağıt mı Makas mı: ")
print("Rakibin Yaptığı:",bilgisayar)

if kullanici == "Taş":
    if bilgisayar == "Kağıt":
        print("Kaybettin!")
    elif bilgisayar == "Makas":
        print("Kazandin!")
    elif bilgisayar == "Taş":
        print("BERABERE")
    else:
        print("HATA")
elif  kullanici == "Makas":
    if bilgisayar == "Taş":
        print("Kaybettin!")
    elif bilgisayar == "Kağıt":
        print("Kazandin!")
    elif bilgisayar == "Makas":
        print("BERABERE")
    else:
        print("HATA")             
elif kullanici == "Kağıt":
    if bilgisayar == "Kağıt":
        print("BERABERE")
    elif bilgisayar ==  "Makas":
        print("kaybettin")
    elif bilgisayar == "Taş":
        print("Kazandin!")
    else:
        print("HATA")         
else:
    print("HATA")
          