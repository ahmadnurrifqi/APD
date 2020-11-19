import os
os.system('cls' if os.name == 'nt' else 'clear')

#TOKO KUE KEJU SULE
#MATERI : PERCABANGAN
print("="*49)
print("|\t\tSELAMAT DATANG DI\t\t|\n|\t\tTOKO KUE KHAS SULE\t\t|")
print("="*49)

print("DAFTAR KUE")
print("1. | 1 KUE KEJU   : Rp 6000")
print("2. | 1 KUE COKLAT : Rp 3500")
print("*DISKON")
print("MEMBELI LEBIH DARI 4 KUE KEJU MENDAPAT DISKON")
print("MEMBELI LEBIH DARI 5 KUE COKLAT MENDAPAT DISKON")
print("")
def kue():
    pilih = input("keju(1) / coklat(2) : ")
    if pilih == '1' :
        keju()
    elif pilih == '2' :
        coklat()
    elif pilih == 'EXIT' :
        exit
    else :
        kue()

def keju():
    jmlh = int(input("JUMLAH : "))
    stock = 25-jmlh
    print ("STOCK  : %d" % (stock))
    print("")
    if jmlh <= -1 :
        keju()
    elif jmlh <=3 :
        print("ANDA TIDAK MENDAPAT DISKON")
        harga = jmlh*6000
        print("TOTAL  : %d" % (harga))
        print("="*48)
        print("|TERIMA KASIH TELAH BERBELANJA DI TOKO KUE KAMI|")
        print("="*48)
    elif jmlh <=15 :
        print("ANDA MENDAPAT DISKON 10%")
        harga = jmlh*6000
        print("HARGA  : %d" % (harga))
        diskon = harga*10/100
        print("DISKON : %d" % (diskon))
        print("")
        total = harga-diskon
        print("TOTAL  : %d" % (total))
        print("="*48)
        print("|TERIMA KASIH TELAH BERBELANJA DI TOKO KUE KAMI|")
        print("="*48)
    elif jmlh <=25 :
        print("ANDA MENDAPAT DISKON 15%")
        harga = jmlh*6000
        print("TOTAL  : %d" % (harga))
        diskon = harga*15/100
        print("DISKON : %d" % (diskon))
        print("")
        total = harga-diskon
        print("TOTAL  : %d" % (total))
        print("="*48)
        print("|TERIMA KASIH TELAH BERBELANJA DI TOKO KUE KAMI|")
        print("="*48)
    elif jmlh >=26 :
        keju()
    else :
        keju()

def coklat():
    jmlh = int(input("JUMLAH : "))
    stock = 35-jmlh
    print ("STOCK  : %d" % (stock))
    print("")
    if jmlh <= -1 :
        coklat()
    elif jmlh <=4 :
        print("ANDA TIDAK MENDAPAT DISKON")
        harga = jmlh*3500
        print("TOTAL  : %d" % (harga))
        print("="*48)
        print("|TERIMA KASIH TELAH BERBELANJA DI TOKO KUE KAMI|")
        print("="*48)
    elif jmlh <=20 :
        print("ANDA MENDAPAT DISKON 7%")
        harga = jmlh*3500
        print("HARGA  : %d" % (harga))
        diskon = harga*7/100
        print("DISKON : %d" % (diskon))
        print("")
        total = harga-diskon
        print("TOTAL  : %d" % (total))
        print("="*48)
        print("|TERIMA KASIH TELAH BERBELANJA DI TOKO KUE KAMI|")
        print("="*48)
    elif jmlh <=35 :
        print("ANDA MENDAPAT DISKON 12%")
        harga = jmlh*3500
        print("TOTAL  : %d" % (harga))
        diskon = harga*12/100
        print("DISKON : %d" % (diskon))
        print("")
        total = harga-diskon
        print("TOTAL  : %d" % (total))
        print("="*48)
        print("|TERIMA KASIH TELAH BERBELANJA DI TOKO KUE KAMI|")
        print("="*48)
    elif jmlh >=36 :
        coklat()
    else :
        coklat()
kue()