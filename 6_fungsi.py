# fungsi dalam python terdapat banyak seperti min() max() dan lainnya
# namun untuk membuat sendiri suatu fungsi dapat dituliskan dengan def
# fungsi sendiri dalam python didefinisikan sebagai objek

# def fungsi1(parameter):
#     aksi

# dalam python ada fungsi yang mempunyai nilai balik dan tidak
# untuk fungsi yang mempunyai nilai balik biasanya diakhir dituliskan return
# def fungsi(parameter):
#     aksi
#     return

#contoh tanpa nilai balik
def fungsi1(a,b):
    c = a + b
    print(c)

hasil = fungsi1(5,10)

#contoh nilai balik
def fungsi2(a,b):
    return a + b

hasil2 = fungsi2(5,10)
print(hasil2)

#terdapat variabel lokal dan global
# variabel lokal = variabel yang cuma bisa diakses di dalam fungsi
# variabel global = variabel yang bisa diakses di dalam dan luar fungsi

#contoh global
g = 10
def vg():
    print(g)

vg()
#contoh lokal
def vk():
    g = 1 #nilai variabel lokal dan tidak akan merubah nilai variabel global
    print(g)
vk()
print(g)

#contoh variabel global yang dapat diedit oleh variabel lokal dengan menuliskan global sebelum pendefinisian variabel

def vgk():
    global g
    g = 2
    print(g)
vgk()
print(g)

# dalam parameter fungsi dapat diberikan nilai defaultnya dan sebaiknya diberikan di parameter terakhir
# karena jika tidak semisal menulis fungsi maka jika parameter default di awal dan parameter tanpa default diakhir
# maka jika kita hanya berniat memasukkan nilai untuk parameter tanpa default, nilai dari yang dimasukkan akan masuk pada parameter default tsb
# dan akan mengakibatkan error karena tidak ada nilai dari parameter tanpa default

def pdf(a , b = 10):
    c = a + b
    return c

hasil3 = pdf(2)
print(hasil3)

# dengan mendefinisikan keyword argument dari parameter kita dapat menuliskan secara tidak urut nilai parameternya
# contoh

def pdf2(a, b):
    c = a + b
    return c

hasil4 = pdf2(b = 2, a = 5)
print(hasil4)

# ada 2 parameter khusus yang di sebut variabel length argument yaitu *args dan **kwargs
# *args digunakan untuk dapat memasukkan nilai parameter sebanyak apapun tanpa disertai keyword arguments nya

def ar(*args):
    for i in args:
        print(i)

hasil5 = ar(10,20,30)

#args dapat dikombinasikan dengan keyword argument dan untuk memasukkan nilainya harus disertai dengan keyword argyments

def ar2(*args, a):
    for i in args, a:
        print(i)

hasil6 = ar2(10,20,30, a = 40)

#**kwargs dapat memasukkan nilai berapapun namun harus disertai keyword arguments nya

def kar(**kwargs):
    for i in kwargs:
        print(i)

hasil7 = kar(a = 10, b =10, c = 20)

# lambda jika  fungsi nilai balik berbentuk mudah atau simple dapat gunakan lamba 

maks = lambda a, b: a if(a>b) else b
print(maks(4,3))

# fungsi dalam fungsi
def f1(g):
    def f2(g):
        return g * 2
    return g, f2(g)

hasil8 = f1(10)
print(hasil8)

# kata kunci non lokal atau mirip global hanya saja non lokal terdapat pada dalam fungsi yang dimana 
# variabel lokal dalam fungsi dan untuk pengambilan data pada fungsi dalam fungsi diperlukan kata kunci non lokal

def f3():
    g = 20
    def f4():
        nonlocal g
        g *= 2
    print(g)
    f4()
    print(g)

f3()

# menjadikan fungsi sebagai parameter

def tambah(*args):
    hasil = 0
    for argm in args:
        hasil += argm
    return hasil

def hitung(fungsi, *args):
    print(f"hasil tambah {fungsi(*args)}")

hitung(tambah, 10,20,30)

# alias fungsi dimana kita bisa memberi nama baru untuk fungsi yang sudah ada seperti print dll
echo = print
echo('python')

# eval dimana fungsi yang digunakan untuk melakukan perhitungan untuk angka dalam bentuk string
halo = '3 + 5'

hasil9 = eval(halo)
echo(hasil9)

# exec fungsi yang digunakan untuk mengeksekusi perintah2 dalam string
halo2 = '''
def halo22():
    print('halo halo')

halo22()
'''
hasil10 = exec(halo2)