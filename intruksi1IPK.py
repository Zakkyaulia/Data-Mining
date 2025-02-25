# Meminta input jumlah mata kuliah
jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))

# Inisialisasi list untuk menyimpan hasil konversi
hasil_konversi = []

# Loop untuk setiap mata kuliah
for i in range(jumlah_mk):
    nama_mk = input(f"Nama mata kuliah ke-{i+1}: ")
    nilai_angka = int(input(f"Nilai angka untuk {nama_mk}: "))
    
    # Konversi nilai angka ke huruf
    if nilai_angka >= 80:
        huruf = 'A'
    elif nilai_angka >= 70:
        huruf = 'B'
    elif nilai_angka >= 55:
        huruf = 'C'
    elif nilai_angka >= 40:
        huruf = 'D'
    else:
        huruf = 'E'
    
    hasil_konversi.append(huruf)

# Menampilkan hasil konversi
print("Hasil konversi nilai:", hasil_konversi)

# Menghitung IPK
konversi_ipk = {'A':4, 'B':3, 'C':2, 'D':1, 'E':0}
total_bobot = sum(konversi_ipk[huruf] for huruf in hasil_konversi)
ipk = total_bobot / jumlah_mk

# Menampilkan IPK dengan 2 angka desimal
print("IPK: {:.2f}".format(ipk))
