# width and multiline


data_nama = "nurdiansyah rizki mubarokah"
data_NPM = 9882405219111012
data_umur = 21
data_jurusan = "Informatika dan teknologi"
angkatan = 2019

#String
#standar
# data_String = f"Nama = {data_nama.title()}, NPM = {data_NPM}, Umur = {data_umur}, Jurusan = {data_jurusan.title()}, Angkatan = {angkatan}"
# print(data_String)

#string multiline
print("\n"+5*"=" +"data string"+ 5*"=")
data_String = f"Nama = {data_nama.title()},\nNPM = {data_NPM},\nUmur = {data_umur},\nJurusan = {data_jurusan.title()},\nAngkatan = {angkatan}"
print(data_String)

#String  multiline (kutip triplets)

print("\n"+5*"=" +"data string"+ 5*"=")
data_String = f"""
nama \t\t= {data_nama:<5}
umur \t\t= {data_NPM:<5}
NPM \t\t= {data_NPM:<5}
jurusan \t= {data_jurusan:<5}
angkatan \t= {angkatan:<5}
"""
print(data_String)