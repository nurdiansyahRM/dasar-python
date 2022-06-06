#latihan list

import enum
list_buku = []
while True:


    judul_buku = input("masukan judul buku :")
    nama_penulis = input("masukan nama penulis buku:" )

    buku_baru = [judul_buku,nama_penulis]
    list_buku.append(buku_baru)

    print(30*"=")
    print("No.\t| judul_buku\t|nama_penulis")
   
    for i,buku in enumerate(list_buku):

        print(f"{i+1}\t|{buku[0]}\t\t|{buku[1]} ")
#         i+=1
#     if(i > 3):
#         break
# print("keluar dari perogram")
    islanjut = input("apakah akan melanjutkan input data : ? (y/n)")
    if islanjut == "n":
        break
print("keluar dari perogram")