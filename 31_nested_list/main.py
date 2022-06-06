#nested list

data_1 = [1,2]
data_2 = [3,4]

data_list = [1,2,3,4]
data_D = [data_1,data_2]

print(f"data list dengan format 1D : \n{data_list}")
print(f"data list dengan format 2D : \n{data_D}")
print(30*"=")
#contoh penggunaan nya seperti : 
data_mahasiswa1 = ["Nurdin","19111012","Informatika"]
data_mahasiswa2 = ["Rifqi","19111025","Informatika"]
data_mahasiswa3 = ["Alif","19111035","Informatika"]

himpunan_data_mhs = [data_mahasiswa1,data_mahasiswa2,data_mahasiswa3]

print(f"himpunan data list mahasiswa -> \n{himpunan_data_mhs}")
print(30*"=")
for mhs in himpunan_data_mhs:
    print(f"nama \t:\t{mhs[0]}")
    print(f"NPM  \t:\t{mhs[1]}")
    print(f"jurusan :\t{mhs[2]}\n")
    
    