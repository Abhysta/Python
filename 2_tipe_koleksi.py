# dalam python terdapat tipe data koleksi yaitu list, tupple, dictionary, set, dan frozenset
# list mirip dengan array dimana data dapat diubah dengan insert, extend, append, remove, clear, dan jika mengganti cukup dengan list[indeks] = nilai baru
# tupple tipe data yang mirip dengan list dimana diawali kurung () dan data bersifat konstan tidak dapat diubah2
# dictionary tipe data yang disertai dengan key dan value

#tipe data koleksi yang tidak mengizinkan duplikasi yaitu set dan frozenset
# set tipe data yang dapat digunakan untuk menyimpan tipe data koleksi lain dan dapat dilakukan perubahan dengan add, remove dan clear
# fronzenset tipe data konstan yang tidak dapat dirubah
#contoh

list1 = [1,2,3]
list1.append(5)
list1.remove(2)
list1[0] = 3
print(list1)

tuple1 = (1,2,3)
print(tuple1)

dictionary1 = {'aku' : 'Kamu'}
dictionary1['kamu'] = 'aku'
print(dictionary1)
del dictionary1['kamu']
print(dictionary1)

set1 = set(list1)
set1.add(10)
set1.remove(3)
set1.add(11)
print(set1)

frozenset1 = frozenset(list1)
print(frozenset1)