import csv
from datetime import date
from prettytable import PrettyTable


class catat_keuangan:
  def __init__(self):
    self.data_keuangan = []

    with open('data_keuangan.csv', 'r') as mycsv:
      my_data = csv.reader(mycsv)
      for baris in my_data:
        self.data_keuangan.append(baris)

  def input_catatan(self):
    tanggal = date.today()
    tipe = str(input('Masukan tipe (outcome/income): ')).lower()
    jumlah = int(input('Masukan jumlah: '))
    kategori = str(input('Kategori: ')).lower()

    if tipe == 'outcome':
      jumlah = -jumlah

    # dict untuk menyimpan input catatan
    input_catatan = ({
        'tanggal': tanggal,
        'tipe': tipe,
        'jumlah': jumlah,
        'kategori': kategori
    })

    # menambahkan dict ke file csv
    with open('data_keuangan.csv', mode='a', newline='') as csvfile:
      nama_kolom = ['tanggal', 'tipe', 'jumlah', 'kategori']
      my_writer = csv.DictWriter(csvfile, fieldnames=nama_kolom)
      my_writer.writerow(input_catatan)

    print('Catatan ditambah!\n')

    self.submenu_catatan()

  def table_catatan(self):
    self.__init__()
    # header table
    kolom = PrettyTable(['No', 'Tanggal', 'Tipe', 'Jumlah', 'Kategori'])

    # input data ke tabel dari list data_keuangan
    no = 1
    for i in self.data_keuangan:
      kolom.add_row([no, i[0], i[1], i[2], i[3]])
      no += 1

    print(kolom)

  def hapus_catatan(self):
    self.table_catatan()

    # hapus data dari list
    hapus = int(input('Masukan nomor catatan yang ingin dihapus: '))
    self.data_keuangan.pop(hapus - 1)

    # tulis ulang list ke csv
    with open('data_keuangan.csv', 'w') as csvfile:
      writer = csv.writer(csvfile)
      writer.writerows(self.data_keuangan)

    print('Catatan berhasil dihapus!\n')

    self.submenu_catatan()

  def edit_catatan(self):
    self.table_catatan()

    nomor = int(input('Masukan nomor catatan yang ingin diedit: '))

    # input data baru
    tanggal = input('Masukan tanggal: ')
    tipe = input('Masukan tipe (outcome/income): ')
    jumlah = int(input('Masukan jumlah: '))
    kategori = input('Masukan kategori: ')

    if tipe == 'outcome':
      jumlah = -jumlah

    edited_row = [tanggal, tipe, jumlah, kategori]

    # edit data dari list
    self.data_keuangan[nomor-1] = edited_row

    # masukan edited_row ke csv
    with open('data_keuangan.csv', mode='w') as file:
      writer = csv.writer(file)
      writer.writerows(self.data_keuangan)

    print('Data berhasil diubah!\n')
    self.submenu_catatan()

  def submenu_catatan(self):
    print('Menu: ')
    print('1. Edit catatan')
    print('2. Hapus catatan')
    print('3. Tambah catatan')
    print('4. Kembali ke menu utama')
    tambah = str(input('Pilih menu: '))

    print('')

    if tambah == '1':
      self.edit_catatan()
    elif tambah == '2':
      self.hapus_catatan()
    elif tambah == '3':
      self.input_catatan()
    elif tambah == '4':
      main()

class laporan_keuangan:

  def __init__(self):
    self.data_income = {}
    self.data_outcome = {}

    with open('data_keuangan.csv', 'r') as csvfile:
      my_data = csv.reader(csvfile)
      for data_row in my_data:
        tipe = data_row[1]
        jumlah = int(data_row[2])
        kategori = data_row[3]

        if tipe == 'income':
          if kategori in self.data_income:
            self.data_income[kategori].append(jumlah)
          else:
            self.data_income[kategori] = [jumlah]
        elif tipe == 'outcome':
          if kategori in self.data_outcome:
            self.data_outcome[kategori].append(jumlah)
          else:
            self.data_outcome[kategori] = [jumlah]
        else:
          pass

  def tabel_income(self):
    table = PrettyTable(['No', 'Kategori', 'Jumlah'])

    no = 1

    for x, y in self.data_income.items():
      total_jumlah = sum(y)
      table.add_row([no, x, total_jumlah])
      no += 1
    print(table)

  def tabel_outcome(self):
    table = PrettyTable(['No', 'Kategori', 'Jumlah'])

    no = 1

    # x untuk key dan y untuk value
    for x, y in self.data_outcome.items():
      total_jumlah = sum(y)
      table.add_row([no, x, total_jumlah])
      no += 1

    print(table)

  def saldo(self):
    total_income = 0
    total_outcome = 0

    for key in self.data_income:
      total_income += sum(self.data_income[key])
    for key in self.data_outcome:
      total_outcome += sum(self.data_outcome[key])

    saldo = total_income - -(total_outcome)

    print(f'Total pemasukan bulan ini: {total_income}')
    print(f'Total pengeluaran bulan ini: {total_outcome}')
    print(f'Sisa saldo bulan ini: {saldo}')

  def print_table(self):
    print('--- Total Pemasukan Bulan Ini ---')
    self.tabel_income()
    print('--- Total Pengeluaran Bulan Ini ---')
    self.tabel_outcome()
    print('')

    self.saldo()

    user_input = input('Kembali ke menu utama? (y/n): ')

    if user_input == 'y':
      print('')
      main()
    else:
      pass

class rencana_keuangan:

  def __init__(self):
    self.kebutuhan = None
    self.keinginan = None
    self.menabung = None

  def input_gaji(self):
    gaji = int(input('Masukan besar gaji perbulan: '))

    self.kebutuhan = int(0.5 * gaji)
    self.keinginan = int(0.3 * gaji)
    self.menabung = int(0.2 * gaji)

    print(f'Anggaran kebutuhan perbulan: {self.kebutuhan}')
    print(f'Anggaran keinginan perbulan: {self.keinginan}')
    print(f'Anggaran menabung perbulan: {self.menabung}')
    print('')
    self.user_input(self.kebutuhan, self.keinginan, self.menabung)

  def user_input(self, x, y, z):
    user_input = input('Tambah rincian anggaran? (y/n): ')

    if user_input == 'y':
      kategori = input('Masukan kategori (kebutuhan, keinginan, menabung): ')

      if kategori == 'kebutuhan':
        self.tambah_rincian(kategori, x)
      elif kategori == 'keinginan':
        self.tambah_rincian(kategori, y)
      elif kategori == 'menabung':
        self.tambah_rincian(kategori, z)
        self.tabungan()
      else:
        pass
        

  def tambah_rincian(self, kategori, x):

    while True:
      deskripsi = input('Masukan deskripsi: ')
      if deskripsi == '':
        break

      budget = int(input('Masukan besar anggaran: '))

      sisa = x - budget
      if sisa < 0:
        print('Anggaran melebihi!')
        break
      else:
        print(f'Sisa anggaran {kategori}: {sisa}')

      x = sisa

      list = {'kategori': kategori, 'deskripsi': deskripsi, 'budget': budget}
      with open('budget_db.csv', 'a') as mycsv:
        kolom = ['kategori', 'deskripsi', 'budget']
        writer = csv.DictWriter(mycsv, fieldnames=kolom)
        writer.writerow(list)

      if x == 0:
        break

    # untuk parameter
    kategori = kategori
    self.tabel_rincian_anggaran(kategori)
    self.user_input(self.kebutuhan, self.keinginan, self.menabung)

  def tabel_rincian_anggaran(self, kategori):
    list = []

    with open('budget_db.csv', 'r') as mycsv:
      my_data = csv.reader(mycsv)
      for row in my_data:
        if row[0] == kategori:
          list.append(row)

    table = PrettyTable(['No', 'Kategori', 'Deskripsi', 'Budget'])

    no = 1
    for i in list:
      table.add_row([no, i[0], i[1], i[2]])
      no += 1

    print(table)

  def tabungan(self):
    nama_tabungan = 'HP baru'
    target = 10000000
    
    list = []

    with open('budget_db.csv', 'r') as mycsv:
      mydata = csv.reader(mycsv)
      for i in mydata:
        if i[0] == 'menabung':
          list.append(i[2])
          
    # menghitung tabungan
    progress = 0
    for i in list:
      progress += int(i)

    # menghitung persentase
    persentase = (progress / target) * 100

    print(f'--- Tabungan {nama_tabungan} ---')
    print(f'Progress: {progress}/10000000')
    print(f'Persentase: {persentase}%')
    print('Semangat menabung!')
  
def main():
  print('---------PROGRAM CATATAN KEUANGAN PRIBADI---------')
  print('Menu:')
  print('1. Catat keuangan')
  print('2. Laporan Keuangan Bulanan')
  print('3. Rencana Keuangan')
  user_input = input('Pilih menu: ')
  print('')

  if user_input == '1':
    catat_keuangan().input_catatan()
  elif user_input == '2':
    laporan_keuangan().print_table()
  elif user_input == '3':
    rencana_keuangan().input_gaji()
  else:
    print('Menu tidak tersedia')


if __name__ == '__main__':
  main()
