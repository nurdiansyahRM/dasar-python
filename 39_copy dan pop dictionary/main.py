# copy dictionary

nama_mhs = {
    "cup" : "ucup surucup",
    "tong": "otong surotong",
    "dung" : "dudung",
    "sep" : "asep"
}

nama_mahasiswa = nama_mhs.copy()
print(f"nama_mhs 1 : {nama_mhs}")
print(f"nama_mhs 2 : {nama_mahasiswa}")
print(30*"=")
nama_mahasiswa["cup"] = "ucup ganteng"
print(f"nama_mhs 1 : {nama_mhs}")
print(f"nama_mhs 2 : {nama_mahasiswa}")
print(30*"=")

# pop dictionary
data_asep = nama_mahasiswa.pop("sep")
print(f"nama_mhs 1 : {nama_mhs}")
print(f"nama_mhs 2 : {nama_mahasiswa}")
print(f"data asep = {data_asep}")

#popitem dictionary
print(30*"=")
data_terakhir = nama_mahasiswa.popitem()
print(f"nama_mhs 1 : {nama_mhs}")
print(f"nama_mhs 2 : {nama_mahasiswa}")

