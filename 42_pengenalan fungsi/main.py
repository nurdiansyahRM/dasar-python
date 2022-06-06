from ast import Break
import os
def garis():
    print(50 *"-")
    
# def hello_world():
#     print("hello world") 

os.system("cls") 
# hello_world()
#fungsi dengan argument(input)
# def fungsi(argument): argument atau paramter
#     badan fungsi 
# def hallo (nama):
#     print(f"hallo {nama}")
# hallo("nurdiansyah")    
# garis()
#program aritmatika
    
def tambah (angka1,angka2):
    hasil = int(angka1 + angka2)
    garis()
    print(f"hasilnya adalah :{hasil}")
    garis()
    return  hasil  

def kurang (angka1,angka2):
    hasil = int(angka1 - angka2)
    garis()
    print(f"hasilnya adalah :{hasil}")
    garis()
    return  hasil  

def kali (angka1,angka2):
    hasil = int(angka1 * angka2)
    garis()
    print(f"hasilnya adalah :{hasil}")
    garis()
    return  hasil  

def bagi (angka1,angka2):
    hasil = angka1 / angka2
    garis()
    
    garis()
    print(f"hasilnya adalah :{hasil}")
    return  hasil  
  
# main program
while True :
    garis()
    print(f"{'ARITMATIKA':^50}")
    garis()
    def main_program():
        print("1.pertambahan")
        print("2.pengurangan")
        print("3.perkalian")
        print("4.pembagian")
        chose = int(input("pilih operasi aritmatika :(1/2/3/4) : "))
        garis()
        if chose == 1:
            angka1 = float(input("masukan bilangan 1:"))   
            angka2 = float(input("masukan bilangan 2:"))
            tambah(angka1,angka2)
        elif chose == 2:
            angka1 = float(input("masukan bilangan 1:"))   
            angka2 = float(input("masukan bilangan 2:"))
            kurang(angka1,angka2)
                    
        elif chose == 3:
            angka1 = float(input("masukan bilangan 1:"))   
            angka2 = float(input("masukan bilangan 2:"))
            kali(angka1,angka2)
                    
        elif chose == 4:
            angka1 = float(input("masukan bilangan 1:"))   
            angka2 = float(input("masukan bilangan 2:"))
            bagi(angka1,angka2)
        else :
            print("mohon maaf pilihan anda tidak tersedia :")               
    main_program()
    islanjut = input("apakah mau melakukan operasi kembali ?(y/n):")
    if islanjut == "n":
        break

print("akhir dari program")
