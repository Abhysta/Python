import fractions
import json
from turtle import backward
from unicodedata import decimal


# variabel dapat berupa apa saja dalam berbagai jenis tipe data baik int string boolean float
# dalam python tidak terdapat variabel konstanta
# pendefinisian variabel dapat dilakukan secara langsung tanpa harus disertai var seperti json
# penamaan variabel tidak boleh diawali angka dan tanda baca
# contoh variabel 

a = 5
b = 5
c = a + b

print(type(a))

# terdapat berbagai tipe data yaitu int string boolean float decimal complex fractions
# int berupa angka
# string berupa teks
# boolean menghasil kan nilai True False
# float untuk nilai angka dengan bilangan rill dengan angka dibelekang koma
# decimal untuk nilai decimal dengan bilangan riil dengan angka dibelakang koma yang banyak seperti PI
# complex untuk nilai imajiner 1 + 3j
# fractions untuk nilai pecahan 1/2
# contoh

a = int(5)
b = str('haloo')
c = True
d = float(1.2)

import decimal
decimal.Decimal(1.1)

e = 3 + 1j

import fractions
f = fractions.Fraction(1,2)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)