# operator dalam bentuk methods

# 1. case String  upper case dan  lower case 

# mengubah String ke uppercase


nama = 'nurdiansyah'
convert_to_upper = nama.upper()
print("normal = " + nama)
print("result convert to Upper case : " + convert_to_upper)

# mengubah String ke lowercase
name = "Otong Surotong GUANTENG!!!!!"
convert_to_lower = name.lower()
print("normal = " + name)
print("result convert to Lower case : " + convert_to_lower)



# 2. pengecekan dengan isx method

club = "persib bandung"
islower = club.islower()
print(club + "\tis lower = " + str(islower))
isupper = club.isupper()
print(club + "\tis Upper = " + str(isupper))

# isalpha() <--- untuk mengecek semua huruf
sepatu  = "Adidas"
checkhuruf = sepatu.isalpha()
print(sepatu + " adalah :" + str(checkhuruf))



# isalnum() <--- huruf dan angka
password = "08machine00"
checkhuruf = password.isalnum()
print(password + " adalah " + str(checkhuruf))

# isdecimal () <--- angka saja
angka = "10"
checkhuruf = angka.isdecimal()
print(angka + " adalah " + str(checkhuruf))

# isspace() <-- spasi, tab, newline \n
var = "aku\nharus pergi"
checkhuruf = var.isspace()
print("hasil dari isspace : " + str(checkhuruf))
# istitle() <-- semua kata dimulai dengan huruf besar

judul = "Aku Ingin Pergi"
checkhuruf = judul.istitle()
print(judul + " adalah : " +str(checkhuruf) )



# 3. mengecek komponen startswith() endwith()
check_start = "Nurdiansyah Rizki".startswith("Nurdiansyah")
check_end = "Nurdiansyah Rizki".endswith("Rizki")

print("Start = " + str(check_start))
print("end = " + str(check_end))

# penggabungan komponen join(),split()
data_kendaraan = ['mobil','motor','bajai']
print("data list sebelum di gabungkan : " + str(data_kendaraan))
var_kendaraan  = ','.join(data_kendaraan)
print("data list sudah digabungkan menggunakan\n komponen join() "+  str(var_kendaraan)) 


var_huruf = "hello,word"
print(var_huruf)
pisah = var_huruf.split(",")
print(pisah)

#alokasi karakter rjust(), ljust(),  center()
# rjust() right justipy rata kanan
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

# left justipy
kiri = "kiri".ljust(10) 
print("'"+kiri+"'")
#center
center = "center".center (10,'-') 
print("'"+center+"'")

# kebalikannya -> strip()
center = center.strip('-')#menghilangkan tanda '-'
print("'"+center+"'")
