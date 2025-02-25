# Meminta input jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))

# Inisialisasi variabel
daftar_belanja = []
total_sebelum_diskon = 0

# Input data barang
for i in range(jumlah_barang):
    nama = input(f"\nNama barang ke-{i+1}: ")
    harga = float(input(f"Harga barang ke-{i+1}: Rp "))
    daftar_belanja.append({"nama": nama, "harga": harga})
    total_sebelum_diskon += harga

# Menghitung diskon
if total_sebelum_diskon > 500000:
    diskon = 15
elif total_sebelum_diskon > 300000:
    diskon = 10
elif total_sebelum_diskon > 200000:
    diskon = 5
else:
    diskon = 0

# Menghitung total setelah diskon
besaran_diskon = total_sebelum_diskon * diskon / 100
total_setelah_diskon = total_sebelum_diskon - besaran_diskon

# Menampilkan output
print("\n=== RINCIAN BELANJA ===")
for item in daftar_belanja:
    print(f"{item['nama']}: Rp {item['harga']:.2f}")

print("\n=== TOTAL PEMBAYARAN ===")
print(f"Total belanja sebelum diskon: Rp {total_sebelum_diskon:,.2f}")
print(f"Diskon yang didapat: {diskon}%")
print(f"Besaran diskon: Rp {besaran_diskon:,.2f}")
print(f"Total yang harus dibayar: Rp {total_setelah_diskon:,.2f}")
