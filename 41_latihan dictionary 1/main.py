#template dictionary mahasiswa
import datetime
import os
import string
import random
mahasiswa_template = {
    'nama' :'nama mahasiswa',
    'nim' : '9888240*********',
    'sks_lulus':0,
    'lahir': datetime.datetime(1111,12,12)
}
data_mahasiswa= {
    
}
while True : 
    os.system("cls")
    print(f"{'SELAMAT DATANG MAHASISWA':^50}")
    print(f"{'DATA MAHASISWA':^50}")
    print(50*"-")

    mahasiswa =dict.fromkeys(mahasiswa_template.keys())

    mahasiswa['nama'] = input("nama mahasiswa \t: ")
    mahasiswa['nim']  = input("masukan NIM \t:")
    mahasiswa['sks_lulus'] = (int(input("masukan SKS \t:")))
    TAHUN_LAHIR = int(input("tahun lahir (YYYY):"))
    BULAN_LAHIR = int(input("bulan lahir (1-12):"))
    TANGGAL_LAHIR = int(input("tanggal lahir (1-31):"))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR).strftime('%x')
    print(50*"-")
    KEY = ''.join((random.choice(string.ascii_lowercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})
    print(f"\n{'KEY' :<6} {'Nama' :<20} {'NIM':<10} {'SKS':<8} {'lahir':<10}")        
    print(60*"-")
    
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
    
        NAMA =data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR =data_mahasiswa[KEY]['lahir']
        print(f"{KEY :<6} {NAMA :<20} {NIM:<10} {SKS:<8} {LAHIR:<10}")
    isdone = input("melakukan perulangan kembali?(y/n) :")
    if isdone == "n":
        break

print("ini adalah akhir program terimakasih")



# print(50*"-")
 
# print(f"{mahasiswa['nama'] :^20}| {mahasiswa['nim']:<10}| {mahasiswa['sks_lulus']:<5}| {mahasiswa['lahir']:<10}|")
