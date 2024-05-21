import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Parola uzunluğu:"))
sifre = ""

if uzunluk <= 5:
    uyari = input("Uyarı: 5 hane veya 5 haneden küçük bir şifre tahmin edilebilir. Yine de devam edecek misiniz? evet, iptal ")
    if uyari == "evet":
        for i in range(uzunluk):
            sifre = sifre + random.choice(karakterler)

        print(sifre)
        
    if uyari == "iptal":
        print("Tamam. İptal ettim")
else:
    for i in range(uzunluk):
        sifre = sifre + random.choice(karakterler)

    5
    print(sifre)
            
