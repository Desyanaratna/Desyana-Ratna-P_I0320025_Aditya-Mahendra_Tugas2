#menampilkan informasi data diri
Nama = "Desyana Ratna Pinasthi"
Nama_panggilan = "Desy"
Status = "mahasiswa"
Jurusan = "Teknik Industri"
Angkatan = "2020"
Fakultas = "Teknik"
Universitas = "Universitas Sebelas Maret"
NIM = "I0320025"
Kelas = "A"
Asal_sekolah = "SMA N 1 Boyolali"
Jalur_masuk = "SBMPTN"
Tempat_tanggal_lahir = "Jakarta, 9 Januari 2002"
Tanggal_lahir = 9
Bulan_lahir = 1
Tahun_lahir = 2002
Tanggal_sekarang = 12
Bulan_sekarang = 3
Tahun_sekarang = 2021
U_tahun =int(Tahun_sekarang - Tahun_lahir)
U_bulan = int(Bulan_sekarang - Bulan_lahir)
U_hari = int(Tanggal_sekarang - Tanggal_lahir)
Agama = "Islam"
Kota_lahir = "Jakarta"
Kota_tinggal = "Boyolali"
Dusun = "Kragan"
Rt = 7
Rw = 3
Desa = "Catur"
Kecamatan = "Sambi"
Kabupaten = "Boyolali"
Nama_ayah = "Bambang Purwanto"
Nama_ibu = "Dewi Nurul Rofiah"
Saudara = "tunggal"
Tinggi_badan = 1.62
Berat_badan = 55.2
BMI = float(Berat_badan / (Tinggi_badan ** 2))
Ukuran_sepatu = 38
Size_baju = "M/L"
Warna_baju = "monokrom atau coklat"
Warna_fav = "biru dan hijau"
Makanan_fav = "mie ayam"
Minuman_fav = "ice lemon tea"
Hobi = "menggambar, membaca, mendengarkan musik, dan menonton film ataupun anime"
Music_fav = "Rewrite The Stars, Utakata hanabi dan Dynamite"
Genre_film_fav = "Fantasy dan Action"
Film_fav = "Narnia, X-men series, Avengerrs:endgame"
Anime_fav = "Naruto,AOT,dan Haikyuu"

#menampilkan output data identitas diri
print("Namaku",Nama)
print("Aku biasa dipanggil",Nama_panggilan)
print("Sekarang aku adalah seorang",Status)
print("Aku masuk fakultas", Fakultas, "di",Universitas)
print("Aku mengambil jurusan",Jurusan,"dan merupakan angkatan",Angkatan)
print("Aku masuk kelas",Kelas,"dengan NIM",NIM)
print("Asal sekolahku adalah",Asal_sekolah)
print("Aku masuk universitas lewat jalur",Jalur_masuk)
print("Tempat tanggal lahirku adalah",Tempat_tanggal_lahir)
print("Umurku saat ini adalah",U_tahun,"tahun",U_bulan,"bulan",U_hari,"hari")
print("Aku beragama",Agama)
print("Aku lahir di",Kota_lahir)
print("Namun, sejak kecil aku tinggal di",Kota_tinggal)
print("Alamat rumahku di Dusun",Dusun,Rt,"/",Rw,", Desa",Desa,", Kecamatan",Kecamatan,", Kabupaten",Kabupaten)
print("Nama ayahku adalah",Nama_ayah)
print("Sedangkan nama ibuku adalah",Nama_ibu)
print("Aku seorang anak",Saudara)
print("Tinggiku hanya",Tinggi_badan,"m")
print("Berat badanku sekitar",Berat_badan)
print("BMI saya adalah","{:.2f}".format(BMI))
print("Untuk ukuran sepatuku, biasanya berukur",Ukuran_sepatu)
print("ukuran bajuku biasanya",Size_baju)
print("Warna bajuku lebih dominan",Warna_baju)
print("Aku suka warna",Warna_fav)
print("Makanan kesukaanku adalah",Makanan_fav)
print("Minuman kesukaanku adalah",Minuman_fav)
print("Hobiku biasanya",Hobi)
print("Lagu kesukaanku adalah",Music_fav)
print("Aku sangat suka menonton film genre",Genre_film_fav)
print("Beberapa film kesukaanku adalah",Film_fav)
print("Sedangkan anime kesukaanku adalah",Anime_fav)