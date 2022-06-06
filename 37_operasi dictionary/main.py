#operator dictinary

data_dict = {
    "nrm" :"nurdiansyahRM",
    "sule" :"sule sulaiman",
    "al" : "algazali"
}
# print(data_dict)

for i in data_dict:
    print(f"{i}.data -> {data_dict[i]}")
#panjang dictionary

print(30*"=")

Lendict = len(data_dict)
print(f"panjang dictionary : {Lendict}")

print(30*"=")
#mengecek  key exits in data

key = "nrm"
Check = key in data_dict
print(f"apakah {key} ada di data_dict : {Check}")
data_list = ["ahmad","dudung","ujang"]
#mengakses value(read) untuk dictionary dengan get
print(data_list[0]) #mengecek data pada list
print(data_dict.get("nrm"))# mengecek data pada dictionary
print(data_dict.get("ddg","mohon maaf data dictionary tidak ditemukan"))# mengecek data pada dictionary
#data key ddg pada dictionary tidak ada akan memunculkan pesan none atau bisa dengan memunculkan peringatan dengan menambah value dibelakang key
# print(data_dict.get("ddg","mohon maaf data tidak di temukan"))

#mengupdate dan add data dictionary 
# dengan menggunakan by reference
data_dict["sule"] = "sulaiman"
print(data_dict)
data_dict["sep"] = "asep"
print(data_dict)

#dengan menggunakan fungsi update
data_dict.update({"nrm":"Nurdiansyah Rizki Mubarokah"})
print(data_dict)
data_dict.update({"R":" Rizki "})
print(data_dict)
