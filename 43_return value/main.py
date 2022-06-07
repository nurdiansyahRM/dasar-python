#fungsi dengan return value
import imp


import os
os.system("cls")
def tambah (angka1,angka2):
    hasil = int(angka1 + angka2)
    # garis()
    print(f"{angka1} + {angka2} hasilnya adalah :{hasil}")
    # garis()
    return  hasil #fungsi return adalah mengembalikan nilai ke variable
a = tambah(2,4) 
print(f"hasil dari variable a = {a}")