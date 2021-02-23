# Program Cryptarithmetic
# Ryo Richardo 13519193

# Global
count = 0 
start = 0

# fungsi rekursif untuk mencari permutasi
def permut(a, x):

    global count, start
    if (x == 1):
        
        # memeriksa jumlah dari perkalian setiap huruf dengan kodenya
        sum = 0
        for i in range (10):
            sum += i * huruf[kunci[i]]

        # jumlah percobaan
        count += 1

        # jika jumlah operan = jumlah hasil, maka benar
        if (sum == 0):
            bol = True

            # memeriksa digit pertama apakah 0
            for kata in word:
                if (kunci[0] == ord(kata[0])-64):
                    bol = False
            if (kunci[0] == ord(hasil[0])-64):
                bol = False
            

            # jika digit pertama tidak 0, print dan exit program
            if bol:
                # menyimpan angka kode tiap huruf
                for i in range (10):
                    huruf[kunci[i]] = i

                # print semua operan kecuali operan terakhir
                for j in range (len(word)-1):
                    for i in range (len(word[j])):
                        print(huruf[ord(word[j][i])-64], end="")
                    print()
                
                # print operan terakhir
                for char in word[len(word)-1]:
                    print(huruf[ord(char)-64], end="")
                print("+")

                # print garis dan hasil penjumlahan
                print(garis)
                for char in hasil:
                    print(huruf[ord(char)-64], end="")

                # print jumlah percobaan dan waktu program berjalan
                print("\nJumlah percobaan =", count, "kali")
                print("Waktu eksekusi   =", time.time() - start,"detik")
                exit(0)

    # mencari pola permutasi yang baru
    for i in range(x):
        permut(a, x-1)
        if (x % 2 == 1):
            a[0], a[x-1] = a[x-1], a[0]
        else:
            a[i], a[x-1] = a[x-1], a[i]


# MAIN PROGRAM
import time

# inisialisasi array huruf dan kunci 
huruf = [0 for i in range (27)]
kunci = [0 for i in range (10)]

# input nama dan membuka file
nama = str(input("Masukkan nama file yang berada dalam folder test: "))
file = open('../test/' + nama + '.txt', 'r')
lines = file.readlines()

# inisialisasi array untuk menyimpan semua operan
word = ["" for i in range (len(lines) - 2)]

# mengisi array dengan operan (kecuali operan terakhir)
for i in range (len(lines) - 3):
    word[i] = lines[i].strip()

# mengisi array dengan operan terakhir
word[len(lines) - 3] = lines[len(lines) - 3].strip("+\n")

# variabel garis dan hasil
garis = lines[len(lines) - 2].strip()
hasil = lines[len(lines) - 1].strip()

# memulai countdown
start = time.time()

# mengisi kamus huruf yang terpakai ke array huruf.
for kata in word:
    for i in range (len(kata)):
        huruf[ord(kata[i])-64] += 10**(len(kata)-i-1)

for i in range (len(hasil)):
    huruf[ord(hasil[i])-64] -= 10**(len(hasil)-i-1)

# mengisi indeks huruf ke array kunci untuk dipermutasi
idx = 0
for i in range (0, 26):
    if (huruf[i] != 0):
        kunci[idx] = i
        idx += 1

# melakukan permutasi hingga exit program
permut(kunci, 10)