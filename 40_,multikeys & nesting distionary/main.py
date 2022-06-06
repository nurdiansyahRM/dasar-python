import datetime
import os
mahasiswa1 = {
    'nama' : 'NurdiansyahRM',
    'Nim' : '19111012',
    'sks' : 200,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2000,8,8)
}
mahasiswa2 = {
    'nama' : 'rifqi dzulfikar',
    'Nim' : '19111025',
    'sks' : 130,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2000,2,12)
}
mahasiswa3 = {
    'nama' : 'Rohid Subagja',
    'Nim' : '19111023',
    'sks' : 190,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2000,5,6)
}
mahasiswa4 = {
    'nama' : 'ai nuraisah',
    'Nim' : '19111021',
    'sks' : 160,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2000,5,6)
}

data_mahasiswa = {
    'MAH001' : mahasiswa1,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3,
    'MAH004' : mahasiswa4,
}
os.system("cls")
print(f"{'KEY':<6}| {'Nama' :<20}| {'NIM':<10}| {'SKS':<5}| {'beasiswa':<5}| {'lahir':<7}|")


print("-"*67)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    
    NAMA =data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['Nim']
    SKS = data_mahasiswa[KEY]['sks']
    BEASISWA =data_mahasiswa[KEY]['beasiswa']
    LAHIR =data_mahasiswa[KEY]['lahir'].strftime('%x')
    print(f"{KEY:<6}| {NAMA :<20}| {NIM:<10}| {SKS:<5}| {BEASISWA:<5}| {LAHIR:^10}|")
    
    