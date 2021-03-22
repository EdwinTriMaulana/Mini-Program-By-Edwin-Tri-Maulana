import random
angka_random=random.randrange(1,21)	#random angka dari 1-20
while True :					
    print("=== Tebak Angka ===")
    inputan = int(input("Coba Tebak Angkanya (1-20): "))	#user menginputkan angka 1-20
    if inputan == angka_random :	#jika inputan==angka_random maka step ini akan dijalankan
        print("Selamat Tebakan Anda Benar")
        break
    elif inputan < angka_random:	#jika inputan <angka_random maka step ini akan dijalankan
        print ("Tebakan Anda Terlalu Kecil")
    elif inputan > angka_random:	#jika inputan >angka_random maka step ini akan dijalankan
        print ("Tebakan Anda Terlalu Besar")
