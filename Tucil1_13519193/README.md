# Doremi Search Engine
Tugas Kecil 1 Strategi Algoritma Semester 2 Tahun 2020/2021 

## Table of contents
* [Description](#description)
* [How to use](#how-to-use)
* [Inspiration](#inspiration)
* [Contact](#contact)

## Description
Program ini dapat menyelesaikan permasalahan Cryparithmetic hingga 10 digit angka yang dimasukkan. Program ini ditulis dalam bahasa python. Untuk menjalankannya, silahkan install python terlebih dahulu di [sini](https://www.python.org/downloads/)

## How to use
Untuk menjalankan program ini, silahkan jalankan file `cryp.py` pada folder `src`. Kemudian, silahkan masukkan nama file yang berada dalam folder `test` ketika program meminta masukkan. Untuk menambah file baru, silahkan menambahkan file dengan ekstensi txt dalam folder `test`. Beberapa hal yang perlu diperhatikan:

* Ketika program meminta masukkan nama file, cukup tuliskan nama filenya, tidak perlu menuliskan ekstensi. Contoh untuk file bernama `tc1.txt`, cukup tuliskan `tc1`.
* Jika ingin menambah file baru, pastikan mengikuti format penulisan pada file-file sebelumnya. Program hanya akan berjalan untuk 26 huruf kapital saja (A, B, sampai Z). Format penulisan yang benar mengacu pada [spesifikasi](http://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2020-2021/Tugas-Kecil-1-(2021).pdf), dengan tanda tambah (+) berada di akhir barisan operan terakhir.
* Jika mendapat pesan error `No such file or directory` setelah memasukkan nama file, kemungkinan error berasal dari perbedaan format path lokasi file input untuk OS yang berbeda. Program ini dibuat di OS Windows 10, dan belum dites apakah kompatibel dengan OS lain seperti Linux maupun MacOS. Untuk menyelesaikan permasalahan ini, silahkan mengganti potongan kode pada baris ke-79 dari `file = open('../test/' + nama + '.txt', 'r')` menjadi `file = open('./test/' + nama + '.txt', 'r')`. Jika masih belum berhasil, silahkan mencari solusi di internet atau mencoba menjalankan di OS Windows 10 pada device lain.

## Contact
Program ini dibuat oleh:
* Nama    : [Ryo Richardo](https://github.com/ryorichardo)
* NIM     : 13519193
* Jurusan : Teknik Informatika