#class
# mengecek jumlah mahasiswa yang beradad di kelas
class student():
    jumlah_mahasiswa = 0

    def __init__(self,input_name,input_nim,input_jurusan):
        self.name = input_name
        self.nim = input_nim
        self.jurusan= input_jurusan
        student.jumlah_mahasiswa += 1
#main program
name = str(input("masukan nama"))
age = int(input("masukan usia"))
jurusan = str(input("masukan jurusan"))
data1 = student(name,age,jurusan)
data2 = student(name,age,jurusan)
data3 = student(name,age,jurusan)
data4= student(name,age,jurusan)

print("jumlah mahasiswa adalah : > ",student.jumlah_mahasiswa)
# note apa itu intence in python