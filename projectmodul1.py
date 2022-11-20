# PROJECT CAPSTONE MODUL 1, NAMA : KEVIN CANDRAWAN
# TOPIC : BUAT SEBUAH PROGRAM UNTUK PERPUSATAKAAN PEMINJAMAN BUKU

listBuku = [
    {
        'nama' : 'harry potter',
        'tipe' : 'novel remaja',
        'harga' : 1000,
        'tahun' : 2002,
        'penulis' : 'jk.rowling'
    },
    {
        'nama' : 'naruto ep 1',
        'tipe' : 'komik anak',
        'harga' : 1500,
        'tahun' : 2001,
        'penulis' : 'masashi k'
    },
    {
        'nama' : 'one piece',
        'tipe' : 'komik remaja',
        'harga' : 3000,
        'tahun' : 2003,
        'penulis' : 'eiichiro oda'
    },
    {
        'nama' : 'biologi',
        'tipe' : 'Pelajaran',
        'harga' : 2500,
        'tahun' : 2012,
        'penulis' : 'neil a'
    }
]  
# MENU UTAMA
def fiturRead():
    while True:
        masukkanAngka = input('''
            FITUR READ
        
            1. Menampilkan Daftar Buku Yang Tersedia
            2. Menampilkan Harga Sewa Buku Per Harinya
            3. exit program
            masukkan angka yang ingin anda jalankan : ''')
            
        if (masukkanAngka == '1'):
            masukkanOpsi = input('apakah anda ingin melihat buku yang tersedia ? (ya/tidak)')
            if (masukkanOpsi == 'ya'):
                print('Daftar Buku Yang Tersedia')
                print('Index \t|Nama Buku\t|Tipe Buku\t|Tahun\t|Penulis')
                for i in range(len(listBuku)):
                    print('{}\t|{}\t|{}\t|{}\t|{}'.format(i,listBuku[i]['nama'],listBuku[i]['tipe'],listBuku[i]['tahun'],listBuku[i]['penulis']))
            else:
                continue                 
        elif (masukkanAngka == '2'):
            while True:
                indexBuku = int(input('Masukkan Index Buku Yang Ingin Di Pinjam : '))
                if (indexBuku > len(listBuku)-1):
                        print('Index Buku Yang anda input tidak tersedia dalam perpusatakaan')
                elif (indexBuku < len(listBuku)):
                    print('Index \t|Nama Buku\t|Tipe Buku\t|Harga\t|Tahun\t|Penulis')
                    for item in listBuku[indexBuku]:
                        print('{}\t|{}\t|{}\t|{}\t|{}\t|{}'.format(indexBuku,listBuku[indexBuku]['nama'],listBuku[indexBuku]['tipe'],listBuku[indexBuku]['harga'],listBuku[indexBuku]['tahun'],listBuku[indexBuku]['penulis']))
                        break
                break
        elif (masukkanAngka == '3'):
            pertanyaan1= input('apakah anda ingin keluar dari FITUR READ ? (ya/tidak)')
            if (pertanyaan1 == 'tidak'):
                print('OKE, SILAHKAN PILIH OPSI DI BAWAH INI')
            else:
                break  

# MENU CREATE DATA
def fiturCreate ():
    while True:
        masukkanAngka = input('''
            FITUR CREATE

            1. Menambahkan Daftar Buku
            2. exit program
            masukkan angka yang ingin anda jalankan : ''')

        if (masukkanAngka == '1'):
            namaBuku = input('Masukkan Nama Buku Yang Ingin di masukkan : ')
            for i in range(len(listBuku)):
                a = (listBuku[i]['nama'])
                if (namaBuku == a):
                    print('nama buku yang anda masukkan sudah tersedia')
                    break
                else:
                    tipeBuku = (input('Masukkan tipe Buku : '))
                    hargaBuku = int(input('Masukkan Harga Sewa Buku Per Hari : '))
                    tahunBuku = int(input('Masukkan Tahun Buku Di Rilis : '))
                    penulisBuku = (input('Masukkan Nama Penulis Buku : '))
                    pertanyaan2 = input('Apakah anda ingin menyimpan data pada library perpusatakaan ? (ya/tidak) : ')
                    if(pertanyaan2 == 'tidak'):
                        print('oke')
                        break
                    elif(pertanyaan2 == 'ya'):
                        listBuku.append({
                        'nama' : namaBuku,
                        'tipe' : tipeBuku,
                        'harga' : hargaBuku,
                        'tahun' : tahunBuku,
                        'penulis' : penulisBuku
                        })
                        print('Daftar Buku Berhasil Ditambahkan')
                        print('Index \t|Nama Buku\t|Tipe Buku\t|Harga\t|Tahun\t|Penulis')
                        for i in range(len(listBuku)):
                            print('{}\t|{}\t|{}\t|{}\t|{}\t|{}'.format(i,listBuku[i]['nama'],listBuku[i]['tipe'],listBuku[i]['harga'],listBuku[i]['tahun'],listBuku[i]['penulis']))
                        break
        elif(masukkanAngka =='2'):
            pertanyaan3= input('apakah anda ingin keluar dari FITUR CREATE ? (ya/tidak)')
            if (pertanyaan3 == 'tidak'):
                print('OKE, SILAHKAN PILIH OPSI DI BAWAH INI')
            else:
                break                     
# MENU UPDATE DATA
def fiturUpdate ():
    while True:
        masukkanAngka = input('''
            FITUR UPDATE
            
            1. MENGUPDATE DATA BUKU
            2. EXIT PROGRAM
            MASUKKAN ANGKA YANG INGIN ANDA JALANKAN : ''')
            
        if(masukkanAngka == '1'):
            print('Daftar List Buku Yang Tersedia')
            print('Index \t|Nama Buku\t|Tipe Buku\t|Harga\t|Tahun\t|Penulis')
            for i in range(len(listBuku)):
               print('{}\t|{}\t|{}\t|{}\t|{}\t|{}'.format(i,listBuku[i]['nama'],listBuku[i]['tipe'],listBuku[i]['harga'],listBuku[i]['tahun'],listBuku[i]['penulis']))
            indexBuku = int(input('Masukkan Index Buku Yang Ingin Di Update : '))
            if (indexBuku > len(listBuku)-1):
                print('Index Buku Yang anda input tidak tersedia dalam perpusatakaan')
                continue
            elif (indexBuku < len(listBuku)):
                print('Index \t|Nama Buku\t|Tipe Buku\t|Harga\t|Tahun\t|Penulis')
                for item in listBuku[indexBuku]:
                    b = listBuku[indexBuku]
                    print('{}\t|{}\t|{}\t|{}\t|{}\t|{}'.format(indexBuku,listBuku[indexBuku]['nama'],listBuku[indexBuku]['tipe'],listBuku[indexBuku]['harga'],listBuku[indexBuku]['tahun'],listBuku[indexBuku]['penulis']))
                    break
            lanjutUPdate = input('apakah anda ingin melanjutkan UPDATE ? (ya/tidak) : ')
            if(lanjutUPdate == 'ya'):
                while True:
                    inputKolom = input('Masukkan nama Kolom Yang ingin Di Update, (NAMA/TIPE/HARGA/TAHUN/PENULIS)? : ')
                    if(inputKolom == 'nama'):
                        namaBaru = (input('Masukkan Value NAMA BUKU yang baru : '))
                        break
                    elif(inputKolom == 'tipe'):
                        tipeBaru = (input('Masukkan Value TIPE BUKU yang baru : '))
                        break
                    elif(inputKolom == 'harga'):
                        hargaBaru = (int(input('Masukkan Value HARGA BUKU yang baru : ')))
                        break
                    elif(inputKolom == 'tahun'):
                        tahunBaru = (int(input('Masukkan Value Tahun Buku yang baru :')))
                        break
                    elif(inputKolom == 'penulis'):
                        penulisBaru = (input('Masukkan Value PENULIS BUKU yang baru : '))
                        break
                    else:
                        print('Kolom tidak tersedia')
            elif(lanjutUPdate == 'tidak'):
                print('oke silahkan pilih menu di bawah ini')
                continue
            updateData = input('Simpan Update Data ? (ya/tidak): ')
            if(updateData == 'ya'):
                if(inputKolom == 'nama'):
                    listBuku[indexBuku]['nama'] = namaBaru
                elif(inputKolom == 'tipe'):
                    listBuku[indexBuku]['tipe'] = tipeBaru
                elif(inputKolom == 'harga'):
                    listBuku[indexBuku]['harga'] = hargaBaru
                elif(inputKolom == 'tahun'):
                    listBuku[indexBuku]['tahun'] = tahunBaru
                elif(inputKolom == 'penulis'):
                    listBuku[indexBuku]['penulis'] = penulisBaru
                print('Data Sudah Terupdate')
                print('Index \t|Nama Buku\t|Tipe Buku\t|Harga\t|Tahun\t|Penulis')
                for i in range(len(listBuku)):
                    print('{}\t|{}\t|{}\t|{}\t|{}\t|{}'.format(i,listBuku[i]['nama'],listBuku[i]['tipe'],listBuku[i]['harga'],listBuku[i]['tahun'],listBuku[i]['penulis']))

            elif(updateData == 'tidak'):
                continue
        else:
            break
# MENU DELETE
def fiturDelete():
    while True:
        masukkanAngka = input('''
            FITUR UPDATE
            
            1. MENGHAPUS DATA BUKU
            2. EXIT PROGRAM
            MASUKKAN ANGKA YANG INGIN ANDA JALANKAN : ''')
        if(masukkanAngka =='1'):
            print('Index \t|Nama Buku\t|Tipe Buku\t|Harga\t|Tahun\t|Penulis')
            for i in range(len(listBuku)):
                print('{}\t|{}\t|{}\t|{}\t|{}\t|{}'.format(i,listBuku[i]['nama'],listBuku[i]['tipe'],listBuku[i]['harga'],listBuku[i]['tahun'],listBuku[i]['penulis']))
            indexHapus = int(input('Masukkan Index Buku Yang Ingin Dihapus : '))
            if(indexHapus > len(listBuku)-1):
                print('Index Buku Yang anda input tidak tersedia dalam perpusatakaan')
                continue
            elif (indexHapus < len(listBuku)):
                lanjutHapus = input('Apakah anda yakin ? (ya/tidak): ')
                if(lanjutHapus == 'ya'):
                    del listBuku[indexHapus]
                    print('Index {} Sudah Terhapus Dalam List Perpusatakaan'.format(indexHapus))
                    print('Index \t|Nama Buku\t|Tipe Buku\t|Harga\t|Tahun\t|Penulis')
                    for i in range(len(listBuku)):
                        print('{}\t|{}\t|{}\t|{}\t|{}\t|{}'.format(i,listBuku[i]['nama'],listBuku[i]['tipe'],listBuku[i]['harga'],listBuku[i]['tahun'],listBuku[i]['penulis']))
                elif(lanjutHapus == 'tidak'):
                    continue
        elif(masukkanAngka =='2'):
            pertanyaan5= input('apakah anda ingin keluar dari FITUR DELETE ? (ya/tidak)')
            if (pertanyaan5 == 'tidak'):
                print('OKE, SILAHKAN PILIH OPSI DI BAWAH INI')
            else:
                break 
# FUNCTION
while True :
    capstone = input('''
        MENU OPSI PROGRAM CAPSTONE :
        
        1. Fitur Read
        2. Fitur Create
        3. Fitur Update
        4. Fitur Delete
        5. exit program
        Masukkan Angka Menu Yang Ingin Dijalankan : ''')

    if(capstone == '1'):
        fiturRead()
    elif(capstone == '2'):
        fiturCreate()
    elif(capstone == '3'):
        fiturUpdate()
    elif(capstone == '4'):
        fiturDelete()
    elif(capstone == '5'):
        print('\nTerimakasih Sudah Berkunjung \nDitunggu kedatangannya kembali\n')
        break

