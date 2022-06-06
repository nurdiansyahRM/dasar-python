angka = [1,1,1,2,3,3,3,6,5,4,5,2,6,6,4,3]
print(f"data list angka -> \n{angka}")
print(50*"+")
#count data (statistik)
# mencari kemunculan data
jumlah_data_1 = angka.count(1)
jumlah_data_6 = angka.count(6)

print(f"jumlah angka 1 -> : {jumlah_data_1}")
print(f"jumlah angka 6 -> : {jumlah_data_6}")

print(50*"+")

#ambil posisi data list (index)

data = ["Nurdiansyah","rizki","Mubarokah","Ujang"]
print(f"data = {data}")

index_data1 = data.index("Nurdiansyah")
index_data2 = data.index("rizki")

print(f"index data Nurdiansyah -> :{index_data1}")
print(f"index data Rizki -> :{index_data2}")

#mengurutkan list data
print(f"data : {angka}")
angka.sort()
print(f"data : {angka}")

#balik data list
print(f"data sesudah di sort -> \n{angka}")
angka.reverse()
print(f"data sesudah di reverse -> \n{angka}")
