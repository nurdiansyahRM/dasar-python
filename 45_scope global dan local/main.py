#global scope dan local scope
nama_mhs = "ahmad"
npm = "19111012"

def data_mahasiswa(namamhs):
    global nama_mhs #fungsi global ini adalah untuk mengambil value dari scope global
    nama_mhs = namamhs
    print("nama mhs adalah (local) -> :",nama_mhs)
def data_npm(namamhs,nim):
    global nama_mhs,npm
    nama_mhs = namamhs
    npm = nim
    print(f"nama mhs adalah = {nama_mhs}\nnim adalah {npm}") #local

data_npm("bagja","19111025")
print(f"nama mhs adalah = {nama_mhs}\nnim adalah {npm}")#global


# mahasiswa("yuli")
# print("nama mhs global ->",nama_mhs)