import array


print(25 * "=")
print("Toko sumber makmur jaya".title())
print(25* "=")

print("1.\t kode barang yang tersedia = 001")
print("2.\t kode barang yang tersedia = 002")
print("3.\t kode barang yang tersedia = 003")
print("4.\t kode barang yang tersedia = 004")
print("5.\t kode barang yang tersedia = 005")

kdbr = str(input("masukan kode barang  : "))

if kdbr == "001":
    Nama_br = "sabun cuci piring"
    harga_br = 1500
    print(f"{Nama_br}\t RP.{harga_br}" )
    jumlah = int(input("Jumlah  barang: "))
    total = harga_br * jumlah
    
    print(f"""
          kode barang :\t {kdbr}
          Nama barang :\t {Nama_br}
          harga barang :\t {harga_br}
          jumlah barang :\t {jumlah}
          total pembelian :Rp.\t{total,} 
          """)
elif kdbr == "002":
    Nama_br = "sabun cuci muka"
    harga_br = 5000
    print(f"{Nama_br}\t RP.{harga_br}" )
    jumlah = int(input("Jumlah  barang: "))
    total = harga_br * jumlah
    
    print(f"""
          kode barang :\t {kdbr}
          Nama barang :\t {Nama_br}
          harga barang :\t {harga_br}
          jumlah barang :\t {jumlah}
          total pembelian :Rp.\t{total:,} 
          """)
elif kdbr == "002":
    Nama_br = "sabun cuci muka"
    harga_br = 5000
    print(f"{Nama_br}\t RP.{harga_br}" )
    jumlah = int(input("Jumlah  barang: "))
    total = harga_br * jumlah
    
    print(f"""
          kode barang :\t {kdbr}
          Nama barang :\t {Nama_br}
          harga barang :\t {harga_br}
          jumlah barang :\t {jumlah}
          total pembelian :Rp.\t{total:,} 
          """)
elif kdbr == "003":
    Nama_br = "sabun cuci baju"
    harga_br = 3000
    print(f"{Nama_br}\t RP.{harga_br}" )
    jumlah = int(input("Jumlah  barang: "))
    total = harga_br * jumlah
    
    print(f"""
          kode barang :\t {kdbr}
          Nama barang :\t {Nama_br}
          harga barang :\t {harga_br}
          jumlah barang :\t {jumlah}
          total pembelian :Rp.\t{total:,} 
          """)
elif kdbr == "004":
    Nama_br = "sikat gigi"
    harga_br = 2000
    print(f"{Nama_br}\t RP.{harga_br}" )
    jumlah = int(input("Jumlah  barang: "))
    total = harga_br * jumlah
    
    print(f"""
          kode barang :\t {kdbr}
          Nama barang :\t {Nama_br}
          harga barang :\t {harga_br}
          jumlah barang :\t {jumlah}
          total pembelian :Rp.\t{total:,} 
          """)
elif kdbr == "005":
    Nama_br = "pasta gigi"
    harga_br = 4000
    print(f"{Nama_br}\t RP.{harga_br}" )
    jumlah = int(input("Jumlah  barang: "))
    total = harga_br * jumlah
    
    print(f"""
          kode barang :\t {kdbr}
          Nama barang :\t {Nama_br}
          harga barang :\t {harga_br}
          jumlah barang :\t {jumlah}
          total pembelian :Rp.\t{total:,} 
          """)
    
else :
    print("kdbr yang anda masukan tidak ada di menu !!!!!!") 

print("akhri program!!!!!")    
    