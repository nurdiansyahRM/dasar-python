# program kalkulator 

print("++++++++++ development by nurdiansyah +++++++++++")

print("1. tambah");
print("2. kurang")
print("3. bagi")
print("4. kali")
print("5. modulus")

N = int(input(("inputkan jumlah perhitungan : ")))

for i  in range (0,N):
    masukan = input("pilih operasi perhitungan : ")
    if masukan == "tambah":
        a = int(input("input angka 1 :"))
        b = int(input("input angka 2 :"))
        hasil = a + b
        print("hasil operator penjumlahan adalah : ",hasil)
    elif masukan == "kurang":
        a = int(input("input angka 1 :"))
        b = int(input("input angka 2 :"))
        hasil = a - b
        print("hasil operator pengurangan adalah : ",hasil)
    elif masukan == "bagi":
        a = float(input("input angka 1 :"))
        b = float(input("input angka 2 :"))
        hasil = a / b        
        print("hasil operator pembagian adalah : ",hasil)
    elif masukan == "kali":
        a = int(input("input angka 1 :"))
        b = int(input("input angka 2 :"))
        hasil = a * b
        print("hasil operator perkalian adalah : ",hasil)
    elif masukan == "modulus":
        a = float(input("input angka 1 :"))
        b = float(input("input angka 2 :"))
        hasil = a % b
        print("hasil operator modulus adalah : ",hasil)
    else:
        print("operator tidak berada di daftar list")        
