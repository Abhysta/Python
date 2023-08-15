# di dalam python hanya terdapat 2 perulangan yaitu while dan for
# while
# iterasi
# while kondisi:
#     aksi

#contoh
i = 0
while i <= 10:
    print('halo')
    i += 1

#range dapat digunakan untuk memberi nilai awal misal dari ingin nilai 1-10
# dengan menuliskan range(indeks awal, indeks akhir, step)

range(1,10,2)

# for lop
# for indeks in range:
#     aksi

for i in range(10):
    print('hai')

#break
i = 10
while i < 10:
    print(i)
    if i % 2 == 0 : break
    i += 1

#continue
for i in range(10):
    if i % 2 == 0 : continue
    print(i)

#iterator dapat digunakan untuk tipe koleksi seperti list set dll untuk memunculkan isi di dalam dan next dapat digunakan untuk memanggil tiap nilainya
#contoh
list = [10,9,8,7]
itr = list.__iter__()
itr.__next__()