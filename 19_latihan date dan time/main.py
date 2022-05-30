# date and time

import datetime as dt
from sys import builtin_module_names


# print(hari_ini)
# print(f"hari ini adalah hari = {hari_ini:%A}")
# tanggal = dt.date(2000,8,8)
# print(tanggal)

#pendeteksi hari lahir 

print("masukan tanggal, bulan dan tahun lahir : ")
tanggal = int(input("tanggal \t :"))
bulan = int(input("bulan  \t\t:"))
tahun = int(input("tahun  \t\t:"))


tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(tanggal_lahir)
print(tanggal_lahir ,f"hari lahir anda adalah = {tanggal_lahir:%A}")
hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) //30

print(f"umur anda adalah :{umur_tahun} tahun,sisa bulan : {umur_bulan_sisa}" )