            # program input data nilai mahasiswa
            # by development : nurdiansyahRM


# mengambil inputan dengan tipe data Str
from telnetlib import DO
from unicodedata import name

    
biner = bool(int(input("data ada : ")))
print("nama anda adalah : ",biner,"type = ",type(biner))

if biner == 1:
    nama = input("masukan nama anda: ")
    # mengambil inputan dengan tipe data int
    age = int(input("masukan usia anda : "))
    #mengambil inputan dengan tipe data float
    rata_rata =float(input("input nilai rata-rata mahasiswa : "))
    print("nama anda adalah : ",nama,"type = ",type(nama))
    print("usia anda adalah : ",age,"type = ",type(age))
    print("rata-rata nilai anda adalah : ",rata_rata,"type = ",type(rata_rata))

    
else :
    print ("data kosong")
    
    

        
    


