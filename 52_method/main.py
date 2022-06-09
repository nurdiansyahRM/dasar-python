class mahasiswa():
    nama = "nama"

    def belajar(self,kondisi):
        print(self.nama,"sedang belajar",kondisi)

    def warna(self):
        print(self.nama,"suka warna merah")

#main programnya

otong = mahasiswa()
    #merubah nama dari nilai object
otong.nama = "otong surotong"
otong.belajar("dengan baik")
otong.warna()
