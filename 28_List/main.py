#operasi
# list 

data_mahasiswa = ["nurdiansyah","rizki","mubarokah"]

#cara mengambil data dari list

print(f"data pertama -> {data_mahasiswa[0]}")
i = 1
for i in range(3):
    print(f"data ke {i+1}. {data_mahasiswa[i]} ")
    
# mengambil info jumlah data di dalam list
print(20*"=")

panjang_data = len(data_mahasiswa)
print(f"panjang data adalah : {panjang_data}")

print(20*"=")

# manipulas item pada list sesuai posisi

# 1. menambah data pada list
print(f"data mahasiswa sebelum di tambah -> \n{data_mahasiswa}")

# nama_variable.insert(posisi,nama_index)
data_mahasiswa.insert(4,"ahmad")

print(f"data mahasiswa sesudah di tambah -> \n{data_mahasiswa}")
print(20*"=")

#menambah data mahasiswa di akhir
data_mahasiswa.append("rojak")
print(f"data mahasiswa sesudah ditambah di index akhir -> \n{data_mahasiswa}")


# 2.menggabungkan list dengan list lainnya
data_mahasiswabaru = ["eli","susan","asep","irawan"]
data_mahasiswa.extend(data_mahasiswabaru)
print(20*"=")
print(f"hasil dari penggabungan  list {data_mahasiswa}")

# 3. menghapus data di list

print(30*"=")
print(f"data sebelum di hapus {data_mahasiswa}")
data_mahasiswa.remove("eli")
print(f"data sesudah di hapus {data_mahasiswa}")
print(30*"=")

# 4. mengubah data di list
print(f"data sebelum di rubah {data_mahasiswa}")
data_mahasiswa[4] = "solihin"
print(f"data sesudah di rubah {data_mahasiswa}")
print(30*"=")

# 5. meremove data yang paling belakang
print(f"data sebelum di rubah {data_mahasiswa}")
data_mahasiswa.pop()
print(f"data sesudah di pop {data_mahasiswa}")

# 6. sort merupakan fungsi yang tidak mengembalikan nilai tetapi daftar target akan diurutkan

data_mahasiswa.sort()


