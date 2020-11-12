# OPERASI ARITMATIKA
def hitung():
    print("="*35)
    print("KALKULATOR MAHASISWA")
    print("="*35)
    print("DATA MAHASISWA")
    input ("Nama Lengkap: ")
    int(input ("NIM         : "))
    prodi = ["PRODI       :","1. Ilmu Komputer","2. Informatika","3. Sistem Inforamsi"]
    print(prodi[0])
    print(prodi[1])
    print(prodi[2])
    print(prodi[3])
    pilih = input("Masukkan pilihan (1/2/3): ")
    if pilih == '1' :
        print ("Ilmu Komputer")
    elif pilih == '2' :
        print("Informatika")
    elif pilih == '3' :
        print("Sistem Informasi")
    else :
        print("DATA TIDAK VALID !!!")
        hitung()
    print("="*35)
    operasi = ["1. Penjumlahan","2. Pengurangan","3. Pembagian","4. Perkalian"]
    print(operasi[0])
    print(operasi[1])
    print(operasi[2])
    print(operasi[3])
    print("="*35)
    print("Silahkan pilih 1-4")
    print("")

    pilih = input("Masukkan pilihan (1/2/3/4): ")
    print("")

    if pilih == '1':
       print("1. Bilangan bulat")
       print("2. Bilangan desimal")
       pilih = input("Masukkan pilihan (1/2): ")
       print("")
       if pilih == '1' :
           a = int(input("Input Nilai Pertama: "))
           b = int(input("Input Nilai Kedua  : "))
           c = a + b
           print("Hasil %d + %d = %d" % (a,b,c))
       elif pilih == '2' :
           a = float(input("Input Nilai Pertama: "))
           b = float(input("Input Nilai Kedua  : "))
           c = a + b
           print("Hasil %d + %d = %d" % (a,b,c))
       tanya()
    elif pilih == '2':
       print("1. Bilangan bulat")
       print("2. Bilangan desimal")
       pilih = input("Masukkan pilihan (1/2): ")
       print("")
       if pilih == '1' :
           a = int(input("Input Nilai Pertama: "))
           b = int(input("Input Nilai Kedua  : "))
           c = a - b
           print("Hasil %d - %d = %d" % (a,b,c))
       elif pilih == '2' :
           a = float(input("Input Nilai Pertama: "))
           b = float(input("Input Nilai Kedua  : "))
           c = a - b
           print("Hasil %d - %d = %d" % (a,b,c))
       tanya()
    elif pilih == '3':
       print("1. Bilangan bulat")
       print("2. Bilangan desimal")
       pilih = input("Masukkan pilihan (1/2): ")
       print("")
       if pilih == '1' :
           a = int(input("Input Nilai Pertama: "))
           b = int(input("Input Nilai Kedua  : "))
           c = a / b
           print("Hasil %d / %d = %d" % (a,b,c))
       elif pilih == '2' :
           a = float(input("Input Nilai Pertama: "))
           b = float(input("Input Nilai Kedua  : "))
           c = a / b
           print("Hasil %d / %d = %d" % (a,b,c))
       tanya()
    elif pilih == '4':
       print("1. Bilangan bulat")
       print("2. Bilangan desimal")
       pilih = input("Masukkan pilihan (1/2): ")
       print("")
       if pilih == '1' :
           a = int(input("Input Nilai Pertama: "))
           b = int(input("Input Nilai Kedua  : "))
           c = a * b
           print("Hasil %d * %d = %d" % (a,b,c))
       elif pilih == '2' :
           a = float(input("Input Nilai Pertama: "))
           b = float(input("Input Nilai Kedua  : "))
           c = a * b
           print("Hasil %d * %d = %d" % (a,b,c))
       tanya()
    else:
       print("DATA TIDAK VALID !!!")
       hitung()
       
def tanya():
    print("")
    tanya = input("BACK (y/t) ? ")
    if tanya == 'y':
        hitung()
    elif tanya == 't':
        exit
        print("THANK YOU")
        print("="*35)
    else:
        print("EROR")
        print("="*35)

hitung()