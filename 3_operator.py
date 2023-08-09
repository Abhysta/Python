# dalam pyhon terdapat operator diantaranya 
# 1 operator penugasan
a = 15
a += a
a -= a
a *= a
a /= a
a //= a
a %= a
a **= a

# 2 operator aritmatika
a + a; a - a; a * a; a / a; a // a; a % a; a ** a

# 3 operator relasional
a == a
a >= a
a <= a
a != a
a > a
a < a

# 4 operator logika

a and a ; a or a; not a

# 5 operator bitwise
# operator yang bekerja pada bilangan bulat
1 & 3; 1 | 3; ~1; 1 >> 2; 1 << 2;
# dalam operator & sama dengan and dan | sama dengan or dan ~ sama dengan not hanya saja dikhusukan bilangan bulat
# yang perhitungannya dalam bentuk bit
# dan >> yang berarti menggeser 1 bit ke arah kanan atau sama saja dibagi dan << digeser ke arah kiri atau sama dengan dikali

# 6 operator keanggotaan
# in dan not in, in digunakan apakah suatu variabel atau bilangan atau parameter masuk ke dalam anggota variabel atau bilangan atau parameter yang ada
# dan not in digunakan untuk mengecek apakah masuk ke dalam atau tidak jika tidak maka bernilai True kebalikan dari in

data = [10,20,30]
10 in data
40 not in data

# 7 operator identitas
# is dan not is, is digunakan untuk mengecek apakah nilai yang ada, masuk dalam id yang sama jika iya maka bernilai True
# dan is not merupakan kebalikan jika masuk maka bernilai False dan jika tidak masuk maka bernilai True

x = 10
y = 10
z = x

x is y
x is z
z is not x

# 8 operator string
# terdiri dari + yang digunakan untuk menggabungkan dua buah string walaupun dapat digunakan interpolasi variabel untuk menggabungkannya
# yaitu dengan {nama variabel} 

r = 'halo'
s = 'halo'
print(r + ' ' + s)