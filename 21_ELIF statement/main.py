#elif = else if statement
print(10*"="+ "perulangan" + 10*"=")

print("1. \t perkalian")
print("2. \t pembagian")
print("3. \t pertambahan")
print("4. \t pengurangan")
print(30*"=")

pilihan = int(input("masukan operasi aritmatika yang anda inginkan (1,2,3,4)?"))

if pilihan == 1:
    angka1 = float(input("masukan angka 1 : "))
    angka2 = float(input("masukan angka 2 : "))
    hasil = angka1 * angka2
    print(f"hasilnya adalah : {hasil}")
elif pilihan == 2:
    angka1 = float(input("masukan angka 1 : "))
    angka2 = float(input("masukan angka 2 : "))
    hasil = angka1 / angka2
    print(f"hasilnya adalah : {hasil}")
elif pilihan == 3:
    angka1 = float(input("masukan angka 1 : "))
    angka2 = float(input("masukan angka 2 : "))
    hasil = angka1 + angka2
    print(f"hasilnya adalah : {hasil}")
elif pilihan == 4:
    angka1 = float(input("masukan angka 1 : "))
    angka2 = float(input("masukan angka 2 : "))
    hasil = angka1 - angka2
    print(f"hasilnya adalah : {hasil}")
    
else:
    print(f"{pilihan} mohon maaf yang anda inputkan tidak ada di dalam menu")
    
print("akhir program!!!!!")
    
