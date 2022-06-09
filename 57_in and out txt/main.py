#input output file


"""
w = write mode / mode menulis dan menghapus file lama, jika tidak ada file maka akan dibuat file baru
r = read mode only/ hanya bisa baca
a = appending mode/ menambahkan data di akhir baris
r+ = write and read mode
"""

#membuat file txt
file =open("data.txt",'w')
file.write("nama : nurdiansyah \n"
           "universitas : unibi\n"
           "jurusan : informatika\n"
           "By development nurdiansyahRm\n")
file.write("hallo dunia")
file.close()


#membaca file txt
file1 =open("data.txt",'r')
# print(file1.read(10)) #membaca 10 kata
print(file1.readline())

print(file1.readline())

file1.close()

#appending mode
file2 =open("data.txt",'a')
file2.write("\nini menambah data baru")
file2.close()







