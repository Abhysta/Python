# dalam python hanya terdapat satu pemilihan yaitu if else, dan tidak terdapat switch seperti js
# if kondisi : aksi
# contoh
a = 1
b = 5
if a > b : print(a)

# contoh 2
if True: print('haloo')

# cara diatas jika hanya satu kondisi
# jika 2 kondisi membutuhkan else
if a > b :
    print(a)
else:
    print(b)

# jika 3 kondisi atau lebih tambahkan elif
if a > b :
    print(a)
elif a < b:
    print(b)
else:
    print('hasil beda')