#defined function adalah function yang dibuat oleh programmer seperti def jumlah ini
def jumlah (a,b): 
    c = a +b
    return c
print(f"hasilnya dari fungsi jumlah : {jumlah(2,3)}")

'''lambda adalah sebuah expresi untuk membuat fungsi lambda sendiri berasal dari teori kalkulus'''
# build-in function adalah function yang tersedia di dalam bahasa pemrograman atau tools yang dapat diakses
# kali = lambda argumen: argumen
kali = lambda x,y: x+y
hasil = kali(1,2)
print(f"hasilnya dari fungsi lambda adalah = {hasil}")
