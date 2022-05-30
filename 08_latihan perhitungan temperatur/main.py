# program sederhana perhitungan temperatur


# 1. rumus  kelvin ke fahrenheit
# f = 1.8 * (K - 273)+32
# 2. rumus fahrenheit ke kelvin
# 5/9 (°F - 32) + 273. F

celcius = float(input("masukan suhu dalam celcius : "))
print("suhu adalah : ",celcius , "celcius")

print("\n<<<<<< mengubah temperatur kelvin ke fahrenheit >>>>>>>>\n")
#step 1 mengubah celcius ke kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah : ",kelvin , "kelvin")
# step 2 mengubah kelvin ke fahrenheit
fahrenheit = (1.8 * (kelvin - 273)) + 32
print("hasil konversi temperatur kelvin ke fahrenheit adalah : ",fahrenheit ,"fahrenheit")

print("\n<<<<<< mengubah temperatur fahrenheit ke kelvin >>>>>>>>\n")
# step 1 mengubah celcius ke fahrenheit
fahrenheit  = ((5/9) * celcius) + 32 
print("suhu dalam fahrenheit adalah : ",fahrenheit ,"fahrenheit")

# step 2 mengubah fahrenheit ke kelvin
kelvin = (fahrenheit - 32) + 273
print("hasil konversi temperatur fahrenheit ke kelvin adalah : ",kelvin ,"kelvin")
