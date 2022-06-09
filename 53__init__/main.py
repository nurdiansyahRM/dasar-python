class mahasiswa():
    name = "name"
    age = "age"
    npm = ""
    def __init__(self, input_nama,input_age,input_npm):
        self.name = input_nama
        self.age = input_age
        self.npm = input_npm

    def belajar(self,kondisi):
        print(self.name,"doing learning",kondisi)

    def warna(self):
        print(self.name,"like color red")

#main programnya

name = input("input your name :")
age = input("input your age :")
npm = input("input your npm:")
data = mahasiswa(name,age,npm)
print("nama : \t",data.name)
print("age : \t",data.age)
print("npm :\t",data.npm)




    #merubah nama dari nilai object
# otong.nama = "otong surotong"
# otong.belajar("dengan baik")
# otong.warna()
