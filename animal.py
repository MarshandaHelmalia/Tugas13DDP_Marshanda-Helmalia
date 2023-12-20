# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak) buat minimal 3 class child (badak, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method  

# parent class
class animal:
    def __init__(self, name, makanan, hidup, berkembangBiak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak

    def cetak(self):
        print("Nama binatang", self.name, "memakan", self.makanan, "hidup di", self.hidup, "berkembang biak dengan cara", self.berkembangBiak)

# class child 1
class badak(animal):
    def __init__(self, name, makanan, hidup, berkembangBiak, jenisHewan, jenisMakanan ):
        super().__init__(name, makanan, hidup, berkembangBiak)
        self.jenisHewan = jenisHewan
        self.jenisMakanan = jenisMakanan

    def cetak(self):
        super().cetak()
        print("merupakan hewan", self.jenisHewan, "dan jenis golongan makanan", self.jenisMakanan)

# class child 2
class ikan(animal):
    def __init__(self, name, makanan, hidup, berkembangBiak, jenisHewan, jenisMakanan, bergerak, kelompokHewan):
        super().__init__(name, makanan, hidup, berkembangBiak)
        self.jenisHewan = jenisHewan
        self.jenisMakanan = jenisMakanan
        self.bergerak = bergerak
        self.kelompokHewan = kelompokHewan

    def cetak(self):
        super().cetak()
        print("jenis", self.jenisHewan, "dan jenis golongan makanan", self.jenisMakanan, "bergerak menggunakan", self.bergerak, "kelompok hewan", self.kelompokHewan)

# class child 3
# class child 3
class ular(animal):
    def __init__(self, name, makanan, hidup, berkembangBiak, jenisHewan, jenisMakanan, bergerak, kelompokHewan, langka, dilindungi):
        super().__init__(name, makanan, hidup, berkembangBiak)
        self.jenisHewan = jenisHewan
        self.jenisMakanan = jenisMakanan
        self.bergerak = bergerak
        self.kelompokHewan = kelompokHewan
        self.langka = langka
        self.dilindungi = dilindungi

    def cetak(self):
        super().cetak()
        print("jenis", self.jenisHewan, "dan jenis golongan makanan", self.jenisMakanan, "bergerak menggunakan", self.bergerak, "kelompok hewan", self.kelompokHewan, "hewan yang", "langka" if self.langka else "tidak langka", "dan", "dilindungi" if self.dilindungi else "tidak dilindungi")


# objek hewan
b = animal("Badak", "tumbuh-tumbuhan", "darat", "melahirkan")
i = animal("Ikan", "mikroorganisme air", "air", "bertelur")
u = animal("Ular", "daging", "darat", "bertelur")
b.cetak()
i.cetak()
u.cetak()
print("============================================================")
# objek badak
bdk = badak("Badak", "tumbuh-tumbuhan", "darat", "melahirkan", "badak bercula satu", "herbivora")
bdk.cetak()
print("============================================================")
# objek ikan
ikn = ikan("Ikan", "mikroorganisme air", "air", "bertelur", "ikan lele", "omnivora", "patil", "nocturnal")
ikn.cetak()
print("============================================================")
# objek ular
ulr = ular("Ular", "daging", "darat", "bertelur", "ular king kobra", "karnivora", "otot-otot perutnya", "berbisa", "terancam punah", "dilindungi")
ulr.cetak()
