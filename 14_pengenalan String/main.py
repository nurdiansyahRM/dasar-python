from tokenize import String


data = 'nurdiansyah'
print(data)
print(type(data))

#  1. cara membuat String

'''
1.  dengan menggunakan single quoute '...'
2.  dengan menggunakan doublle quoute "..."
'''

data = 'menggunakan single quote'
print(data)
data = "menggunakan double quote"
print(data)

print('"hello , how are you ?"')
print("'hello , how are you ?'")
print("ini adalah hari jum'at")

# 2. menggunakan tanda \
print('mari melaksanakan sholat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\nurdin")

# tab
print("nurdiansyah \t rizki")

# backspace
print("nurdiansyah \brizki")

# newline
print("baris pertama. \n baris kedua")
print("baris pertama. \r baris kedua")
print("baris pertama. \r\n baris kedua")


# 3. String literal atau raw

print('C:\new folder') #akan salah pathnya
print(r'C:\new foler')#menggunakan raw String

#multiline literal String
print("""
      nama : Nurdiansyah
      kelas :IF6A
      """)

#multiline literal String dan Raw 
print(r"""
      nama : Nurdiansyah
      kelas :IF6A
      Website : nurdiansyah_py@gmail.com
      """)
