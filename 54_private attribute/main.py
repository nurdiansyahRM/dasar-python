class mahasiswa():
    name = ""
    age = ""
    npm =""
    __nilai = 0
    def __init__(self,input_name,input_age,input_npm):
        self.name = input_name #atribut public
        self.age = input_age #atribut
        self.npm = input_npm

    def tugas(self,input_tugas):
        self.__nilai += input_tugas

    def uts(self,input_uts):
        self.__nilai += input_uts

    def uas(self,input_uas):
        self.__nilai += input_uas
    def average(self):
        print(self.__nilai)
        value = ((self.__nilai) / 3)
        print(value)
        hasil = int(value)
        if hasil >= 85 and hasil < 100 :
             print("data mahasiswa : \n nama = ", self.name,"age = ",self.age, "npm = ",self.npm,"\n mendapatkan Grade= A")
        elif hasil >= 70 and hasil < 85:
            print("data mahasiswa : \n nama = ", self.name, "age = ", self.age, "npm = ", self.npm,
                  "\n mendapatkan Grade= B")
        elif hasil >= 60 and hasil < 70:
            print("data mahasiswa : \n nama = ", self.name, "age = ", self.age, "npm = ", self.npm,
                  "\n mendapatkan Grade= C")
        else:
            print("data mahasiswa : \n nama = ", self.name, "age = ", self.age, "npm = ", self.npm,
                  "\n mendapatkan Grade= D")
#main program
print(30*"-")
name = input("entry your name : ")
age =  input("entry your age : ")
npm = input("entry your npm:")
value_tugas = int(input("masukan nilai tugas : "))
value_uts = int(input("masukan nilai uts :"))
value_uas = int(input("masukan nilai uas : "))



data = mahasiswa(name,age,npm)
data.tugas(value_tugas)
data.uts(value_uts)
data.uas(value_uas)
data.average()
