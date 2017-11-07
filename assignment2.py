import sys

girilenKelime  = (sys.argv[1])
girilenHarfDizisi = (sys.argv[2].split(','))

#girilenKelime  = input("Oyun kurucu kelime gir :")
#girilenHarfDizisi = ['c','e','y','a','m','q','r']

dizininBoyu = len(girilenHarfDizisi)
kelimeUzunluk = len(girilenKelime)

girilenKdizisi = list(girilenKelime)

oyunModu = "IN"
kalanHak = 5
cekisSayisi = 0
cekilenHarf = ""
ekranDizisi =[]
cekilenHarfDizisiIN = []
cekilenHarfDizisiOUT = []


for i in range(kelimeUzunluk):
    ekranDizisi.append('-')


print("You have", str(kalanHak), "guesses left")
print(ekranDizisi)
print("-"*44)

devamEt = 1
i = 0

while (devamEt)== 1  :
    cekilenHarf = girilenHarfDizisi[cekisSayisi]

    if kalanHak>0:
        if (oyunModu == "IN"):
            if cekilenHarf not in cekilenHarfDizisiIN:
                bulundu=0
                cekilenHarfDizisiIN.append(cekilenHarf)
                for i in range(0,len(girilenKdizisi)):
                    if cekilenHarf == girilenKdizisi[i]:
                        bulundu=1
                        ekranDizisi[i]=cekilenHarf
                if bulundu !=1:
                    oyunModu = "OUT"
                    kalanHak = kalanHak - 1
                    print("Guessed word:", cekilenHarf, " The game turned into OUT mode")
                    print(" You have", kalanHak, " guesses left")
                else:
                    print("Guessed word:", cekilenHarf, " You are in IN mode")
                    print(" You have", kalanHak, " guesses left")
                print(ekranDizisi)
                print("-" * 44)
            else:
                oyunModu = "OUT"
                kalanHak=kalanHak - 1
                print("Guessed word:", cekilenHarf , " is used in IN mode. The game turned into OUT mode")
                print(" You have", kalanHak, " guesses left")
                print(ekranDizisi)
                print("-" * 44)
        elif (oyunModu == "OUT"):
            if cekilenHarf not in cekilenHarfDizisiOUT:
                bulundu = 0
                cekilenHarfDizisiOUT.append(cekilenHarf)
                if cekilenHarf in girilenKdizisi:
                    oyunModu = "OUT"
                    kalanHak = kalanHak - 1
                    print("Guessed word:", cekilenHarf , " You are in OUT mode")
                else:
                    oyunModu = "IN"
                    bulundu=0
                    print("Guessed word:", cekilenHarf, " The game turned into IN mode")
                print(" You have", kalanHak, " guesses left")
                print(ekranDizisi)
                print("-" * 44)
            else:
                print("Guessed word:", cekilenHarf , " is used in OUT mode. You are in OUT mode")
                kalanHak = kalanHak - 1

    cekisSayisi = cekisSayisi + 1
    if ekranDizisi == girilenKdizisi:
        print("")
        print("You won the game")
        devamEt=0
    elif kalanHak == 0 :
        print("")
        print("You lost the game")
        devamEt=0
    elif cekisSayisi > (dizininBoyu - 1):
        print("")
        print("You finished all letters")
        print("You lost the game")
        devamEt=0
