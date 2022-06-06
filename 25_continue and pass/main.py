#control flow
#  pass -> berfungsi sebagai dummy tidaka akan di eksekusi


# angka = 0
# while angka < 5:
    # angka+=1
    # 
    # if angka ==3:
        # pass
    # 
    # print(angka)
        # 

# continue

angka = 0

print(f"angka sekarang ->{angka}")

while angka < 5 :
      angka +=1
      print(f"angka sekarang ->{angka}")
      
      if angka == 2:
        print("Python")
        continue
    
      print("oke mantap")
print("finish")