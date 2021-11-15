# Nama = "Yudistira Dwi Anggara" #String karena huruf
# NIM = 212410102085 #Integer karena angka
# Umur = "18" 
# Umur = int(Umur) #Tipe Data Umur dirubah dari string ke integer
# TinggiBadan = 1.74 #Float karena bilangan desimal jika integer maka angka setelah koma akan dibulatkan
# BeratBadan = 55 #Integer karena angka
# StatusKejombloan = "Jomblo karena ditikung temen :(" #String karena huruf

# if BeratBadan == 55 :
#     cek = True #Tipe Data Boolean untuk mengecek 
# else:
#     cek = False 

# print(Nama, NIM, Umur, TinggiBadan, BeratBadan, StatusKejombloan, cek)
# print(type(Nama), type(NIM), type(Umur), type(TinggiBadan), type(BeratBadan),type(StatusKejombloan),type(cek))

# var=1
# print(var)
# var += 1
# print(var)

# x= "18+"
# print(x)
# print(type(x))

# def myfunc():
#   global x
#   x = "fantastic"

# bilangan : int(input("masukan bilangan: "))
# a = 1
# while a <= len (bilangan) :
#   jumlah = bilangan [0] + bilangan [1] + bilangan [2]
#   print (jumlah)
#   print ("Ya")
# else :
#   print ("Tidak")


# Bilangan = int(input())
# a = 0

# for i in str(Bilangan):
#     a = int(i) + a
# print (a)
# if Bilangan % a != 0 :
#     print ('Tidak')
# else :
#     print ('Ya')

# Bilangan=int(input())
# n = Bilangan
# total=0
# while(n>0) :
#   digit=n%10
#   total=total + digit
#   n=n//10
# if Bilangan % total != 0 :
#   print ("Tidak")
# else :
#   print ("Ya")

# angka=int(input())
# a=angka/100
# b=int((angka/10))%10
# c=angka%10
# if int(angka)%int((a+b+c))==0 :
#     print("Ya")
# else :
#     print("Tidak")

# Bilangan : int(input())
# n = Bilangan

# for i in str(Bilangan):
#   a = int(i)
#   print (a)
#   a += 1

Nilai = 0

Batas = 1

n = int(input())

for i in range(n):

    for kolom in range(0, Batas):

        print(Nilai, end=' ')
        if Nilai < 9 :
          Nilai += 1
        else :
          Nilai = 0

    print(" ")
    Batas += 1

n = int(input())

print (n*2)

def Advanced(Angka):
    if Angka == 0:
        return 0
    elif Angka == 2:
        return 4
    elif Angka == 1:
        return 2
    else:
        return Advanced(Angka-2) + Advanced(Angka-1)
print(Advanced(int(input())))