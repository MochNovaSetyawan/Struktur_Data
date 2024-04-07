# Buat struct :
# NIM, Nama, Alamat, Tempat, TanggalLahir
# Alamat merupakan struct yang terdiri dari NamaJalan, NomorRumah, Kota, Provinsi
# TanggalLahir merupakan struct yang berisi Tanggal, Bulan, Tahun


class alamat:
    def __init__(self, NamaJalan, NomorRumah, Kota, Provinsi):
        self.NamaJalan = NamaJalan
        self.NomorRumah = NomorRumah
        self.Kota = Kota
        self.Provinsi = Provinsi

class tanggalLahir:
    def __init__(self, Tanggal, Bulan, Tahun):
        self.Tanggal = Tanggal
        self.Bulan = Bulan
        self.Tahun = Tahun

class mahasiswa:
    def __init__(self, Nama, Alamat, Tempat, TanggalLahir):
        self.Nama = Nama
        self.Alamat = Alamat
        self.Tempat = Tempat
        self.TanggalLahir = TanggalLahir

    def TampilanInfo(self):
        print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(f"Nama                    = {self.Nama}")
        print(f"Alamat                  = Jln.{self.Alamat.NamaJalan}, No.{self.Alamat.NomorRumah}, Kota {self.Alamat.Kota}, Prov.{self.Alamat.Provinsi}")
        print(f"Tempat,Tanggal Lahir    = {self.Tempat}, {self.TanggalLahir.Tanggal} {self.TanggalLahir.Bulan} {self.TanggalLahir.Tahun}")
        print(f"++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def Input():
    Nama        =     input("Masukan Nama   :")

    print("Alamat")
    NamaJalan   =     input("Nama Jalan     :")
    NomorRumah  =     input("Nomor Rumah    :")
    Kota        =     input("Kota           :")
    Provinsi    =     input("Provinsi       :")

    print("Tanggal Lahir")
    Tempat      =     input("Tempat         :")
    Tanggal     = int(input("Tanggal        :"))
    Bulan       = str(input("Bulan          :"))
    Tahun       = int(input("Tahun          :"))

    Alamat = alamat(NamaJalan, NomorRumah, Kota, Provinsi)
    TanggalLahir = tanggalLahir(Tanggal, Bulan, Tahun)
    return mahasiswa(Nama, Alamat, Tempat, TanggalLahir)


daftarMahasiswa = Input()
daftarMahasiswa.TampilanInfo()