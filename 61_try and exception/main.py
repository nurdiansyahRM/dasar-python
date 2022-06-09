# error dibagi 2 :
# 1. runtime error
# 2. error yang dideteksi interpreter (systax error)


#
# try:
#     a = 1/0
# except:
#     print("ini menangkap error zero divided")
#
# print("this is end program ")
while True :
    try:
        angka1 = int(input("masukan angka 1 "))
        angka2 = int(input("masukan angka 2 "))
        hasil = angka1 / angka2
        break
    except ValueError:
        print("yang anda masukan bukan angka")
    except ZeroDivisionError:
        print("anda memasukan angka 0 coba angka yang lain selain 0 ")
    except Exception as e:
        print(e)

print("this is end program in python keep smile coding")


"""
type of exception errors:
1. IOError
2. ImportError
3. ValueError
4. Division by Zero
5. KeyboardInterupted
6. EOFError

"""