#menampilkan informasi program
print("Menghitung Luas Persegi Panjang")

#input data nilai panjang dan lebar
Panjang = float(input("Masukkan nilai Panjang: "))
Lebar = float(input("Masukkan nilai lebar: "))

#memproses data luas persegi panjang
Luas_persegi_panjang = Panjang * Lebar

#ouput perhitungan luas persegi panjang
print("Luas persegi panjang adalah",Luas_persegi_panjang)

#menampilkan informasi program
print("Menghitung Luas Lingkaran")

#input data jari-jari lingkaran
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

#memproses data luas lingkaran
Luas_lingkaran = 3.14 * jari_jari

#ouput perhitungan luas lingkaran
print("Luas lingkaran adalah",Luas_lingkaran)

#menampilkan informasi program
print("Menghitung Luas Kubus")

#input data sisi sisi kubus
sisi = float(input("Masukkan nilai sisi kubus: "))

#memproses data luas kubus
Luas_kubus = 6 * (sisi ** 2)

#ouput perhitungan luas kubus
print("Luas kubus adalah",Luas_kubus)

#menampilkan informasi program
print("Konversi suhu Celcius ke Fahrenheit")

#input nilai suhu dalam celcius
C = float(input("Masukkan suhu dalam celcius: "))

#melakukan proses konversi suhu ke fahrenheit
F = 9 * (C + 32)/ 5

#output nilai konversi suhu
print("Celcius: ", C)
print("Fahrenheit: ", F)

#menampilkan informasi program
print("Konversi suhu Reamur ke Kelvin")

#input nilai suhu dalam reamur
R = float(input("Masukkan suhu dalam reamur: "))

#melakukan proses konversi suhu ke kelvin
K = 5 * R / 4 + 273

#output nilai konversi suhu
print("Reamur: ", R)
print("Kelvin: ", K)
