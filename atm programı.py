print("""

ZG Coin'e Hoşgeldiniz

işlemler:

1.Coin Sorgulama

2.Coin Yatırma

3.Coin Çekme

ZG Coinden Çıkmak İçin 'q' ya Basınız

""")

bakiye = 1000

while True:
    işlem = input("İşleminizi Seçiniz: ")


    if (işlem == "1"):
        print("Coin miktarınız: ",bakiye)
    elif (işlem == "2"):
        miktar = int(input("Coin Yatırma Miktarını Giriniz: "))
        bakiye += miktar
        a = bakiye
        print("Güncel Coininiz = ",a)
    elif (işlem == "3"):
        miktar2 = int(input("Coin Çekme Miktarını Giriniz: "))
        bakiye -= miktar2
        b = bakiye
        if (bakiye - b < 0):
            print("işlem geçersiz")

    elif (işlem == "q"):
        print("Bizi Tercih Ettiğiniz İçin Teşekkürler...")
        break
    else:
        print("Geçersiz İşlem...")











