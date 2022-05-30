# format String

# contoh generic
# ini merupakan code yang tidak menggunakan format
# note : Fungsi format() berfungsi untuk melakukan pengaturan format string yang akan dicetak atau ditampilkan ke monitor.
#1. String <class Str>


nama ="ucup"
str = "hello " + nama
print("normal = "+ str)

# contoh penggunaan fungsi format()
nama = "rizki"
format_str = f"hallo {nama}"
print("fortmat = " + format_str)


#boolean <class bool>
bool = True
format_str = f'boolean = {bool}'
print(format_str + " = " ,type(format_str))

#integer <class int>
angka = 10
format_str = f'angka = {angka}'
print(format_str + " = " ,type(format_str))

#bilangan bulat
angka = 15
format_str = f'bilangan bulat =  {angka:d}'
print(format_str)

#bilangan ribuan
angka = 2000
format_str = f"bilangan ribuan = {angka:,}"
print(format_str) 

#bilangan puluhan
angka = 20000
format_str = f"bilangan puluhan = {angka:,}"
print(format_str) 

#bilangan ratusan
angka = 200000
format_str = f"bilangan ratusan = {angka:,}"
print(format_str) 

#bilangan jutaan
angka = 2000000
format_str = f"bilangan jutaan = {angka:,}"
print(format_str) 


#bilangan decimal
angka = 2000.54321
format_str = f"bilangan decimal = {angka:.2f}"
print(format_str) 


#menampilkan leading zero
angka = 2000.54321
format_str = f"bilangan decimal = {angka:09.2f}"
print(format_str) 

#menampilkan tanda + dan minus - 
angka_minus = -10
angka_plus = -10.21212
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus) 
print(format_plus)


angka_persen = 10.212
format_persen = f"persentase {angka_persen:.2%}"
print(format_persen)

#melakukan operasi aritmatika di dalam placeholder 
harga = 10000
jumlah = 5

format_String = f"harga total = Rp.{harga*jumlah:,}"
print(format_String)

# format angka lain (binary,octa,hex)

angka = 255
format_binary = f"binary = {bin(angka)}"
format_octa = f"octal = {oct(angka)}"
format_hex = f"octal = {hex(angka)}"

print(format_binary)
print(format_octa)
print(format_hex)