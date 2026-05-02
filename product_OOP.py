class Produk :
  def __init__(self,nama,harga,stok) :
    self.__nama = nama
    self.__harga = harga
    self.__stok = stok
  def get_nama(self) :
    return self.__nama
  def get_harga(self) :
    return self.__harga
  def get_stok(self):
    return self.__stok
  def set_harga(self,jumlah_harga) :
    if jumlah_harga >= 0 :
      self.__harga = jumlah_harga
    else :
      print("Harga tidak boleh negatif")
  def set_stok(self,jumlah_stok):
    if jumlah_stok >= 0 :
      self.__stok = jumlah_stok
    else :
      print("Stok tidak boleh negatif")
class Elektronik(Produk) :
  def __init__(self,nama,harga,stok,garansi) :
    super().__init__(nama,harga,stok)
    self.__garansi = garansi 
  def info(self) :
    print(f"Nama : {self.get_nama()}")
    print(f"Harga : {self.get_harga()}")
    print(f"Stok : {self.get_stok()}")
    print(f"Garansi : {self.__garansi}")
class Makanan(Produk) :
  def __init__(self,nama,harga,stok,expired):
    super().__init__(nama,harga,stok)
    self.__expired = expired
  def info(self) :
    print(f"Nama : {self.get_nama()}")
    print(f"Harga : {self.get_harga()}")
    print(f"Stok : {self.get_stok()}")
    print(f"Expired : {self.__expired}")

elektro1 = Elektronik("AC", 3000000,30,"5 Tahun")
makan1 = Makanan("Pizza",50000,300,2027)

elektro1.set_harga(-20)
makan1.set_stok(-3)

list_produk = [elektro1,makan1]
for produk in list_produk :
  produk.info()