# gaji per jam = 5000
# jika lebih dari 7 jam maka di anggap lembur
# gaji per jam lembur = 15 x gajian per jam.
# gunakan struct untuk membuat program tersebut

class Gaji:
    def __init__(self):
        self.jumlahJamKerja = int(input("Masukan jumlah jam kerja: "))
        self.gajiPerjam = 50000

    def kalkulasiSalary(self):

        if self.jumlahJamKerja <= 7 :
            gajiNormal = self.gajiPerjam * self.jumlahJamKerja
            return gajiNormal
        
        elif self.jumlahJamKerja >7 :
            gajiNormal = self.gajiPerjam * 7
            lemburPerjam = self.jumlahJamKerja - 7
            gajilembur = 15 * self.gajiPerjam * lemburPerjam
            return gajilembur + gajiNormal

    def tampilan(self):
        print(f"Jam kerja: {self.jumlahJamKerja}")
        print(f"Gaji yang diperoleh: {self.kalkulasiSalary()}")

gajiKaryawan = Gaji()
gajiKaryawan.tampilan()
