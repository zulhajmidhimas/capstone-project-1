allData = [
    {
        'kelas' : 'A',
        'nis' : 10001,
        'nama' : 'Anna',
        'tugas' : 100,
        'UTS' : 85,
        'UAS' : 85
    },
    {
        'kelas' : 'B',
        'nis' : 10002,
        'nama' : 'Ben',
        'tugas' : 80,
        'UTS' : 75,
        'UAS' : 95
    },
    {
        'kelas' : 'C',
        'nis' : 10003,
        'nama' : 'Chris',
        'tugas' : 90,
        'UTS' : 75,
        'UAS' : 85
    },
]

def headerPrint():
    print('\nDaftar Nilai Siswa\n')
    print('\033[1mNo.\t|Kelas\t\t|NIS\t\t|Nama\t\t|Tugas\t\t|UTS\t\t|UAS \033[0m ')

def headernoindexPrint():
    print('\nDaftar Nilai Siswa\n')
    print('\033[1m Kelas\t\t|NIS\t\t| Nama\t\t| Tugas\t\t| UTS\t\t| UAS \033[0m ')

def alldataPrint():
    headerPrint()
    for i in range(len(allData)):
        print('{}\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}'.format(i+1, allData[i]['kelas'], allData[i]['nis'], allData[i]['nama'], allData[i]['tugas'], allData[i]['UTS'], allData[i]['UAS']))

def falseformat():
    print('''
    =============================================
    Input yang anda masukkan tidak sesuai format.
    =============================================
    ''')

# FUNCTION TAMPILKAN DATA
def readMain():
    readselect=input("""

        Data yang ingin ditampilkan:
        1. Tampilkan Data seluruh siswa
        2. Berdasarkan Kelas
        3. Kembali ke halaman utama

        Masukkan angka menu yang dipilih: """)
    if readselect=='1':
        alldataPrint()
    elif readselect=='2':
        read_classSelect=(input('''
                
        Daftar Kelas:
        A. Kelas A
        B. Kelas B
        C. Kelas C
        D. Kembali ke halaman utama

        Masukkan Kelas yang akan ditampilkan: ''')).upper()
        if read_classSelect=='A':
            headerPrint()
            for y in range(len(allData)):
                if (allData[y]['kelas'])=='A':
                    print('{}\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}'.format(y, allData[y]['kelas'], allData[y]['nis'], allData[y]['nama'], allData[y]['tugas'], allData[y]['UTS'], allData[y]['UAS']))
        elif read_classSelect=='B':
            headerPrint()
            for y in range(len(allData)):
                if (allData[y]['kelas'])=='B':
                    print('{}\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}'.format(y, allData[y]['kelas'], allData[y]['nis'], allData[y]['nama'], allData[y]['tugas'], allData[y]['UTS'], allData[y]['UAS']))
        elif read_classSelect=='C':
            headerPrint()
            for y in range(len(allData)):
                if (allData[y]['kelas'])=='C':
                    print('{}\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}'.format(y, allData[y]['kelas'], allData[y]['nis'], allData[y]['nama'], allData[y]['tugas'], allData[y]['UTS'], allData[y]['UAS']))
        elif read_classSelect=='D':
            mainPage()
    elif readselect=='3':
        mainPage()
    else:
        print('Menu yang anda pilih tidak tersedia. Anda akan diarahkan kembali ke halaman utama.')
        mainPage()
    
# FUNCTION TAMBAH DATA
def createMain():
    while True:
        createclass=input('Masukkan kelas siswa: ').upper()
        try:
            if createclass == '':
                falseformat()
                createMain()
        except ValueError:
            falseformat()
        else:
            break
    while True:
        createnis=int(input('Masukkan nomor induk siswa (5 angka, contoh: 100XX): '))
        try:
            if createnis == '':
                falseformat()
                createMain()
        except ValueError:
            falseformat()
        else: #equal to createnis.isnumeric()
            break
    while True:
        createname=input('Masukkan nama siswa: ').capitalize()
        try:
            if createname == '':
                falseformat()
        except ValueError:
            falseformat()
        else:
            break
    while True:
        createtugas=int(input('Masukkan nilai tugas siswa: '))
        try:
            if createtugas == '':
                falseformat()
        except ValueError:
            falseformat()
        else:
            break
    while True:
        createuts=int(input('Masukkan nilai UTS siswa: '))
        try:
            if createuts == '':
                falseformat()
        except ValueError:
            falseformat()
        else:
            break
    while True:
        createuas=int(input('Masukkan nilai UAS siswa: '))
        try:
            if createuas == '':
                falseformat()
        except ValueError:
            falseformat()
        else:
            break
    headernoindexPrint()
    print('{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t| {}'.format(createclass,createnis,createname,createtugas,createuts,createuas))
    create_option=input('Apakah data yang dimasukkan sudah benar? (y/n): ')
    if create_option=='y':
        allData.append({

            'kelas': createclass,
            'nis': createnis,
            'nama': createname,
            'tugas': createtugas,
            'UTS' : createuts,
            'UAS' : createuas
        })
        alldataPrint()
        print('\nTerima kasih, data berhasil dimasukkan.')
    elif create_option=='n':
        print('\nAnda akan diarahkan kembali ke menu utama.')

# FUNCTION UBAH DATA
def updateMain():
    while True:
        alldataPrint()
        updateselect=input(""" 
        ==========UPDATE NILAI SISWA==========

        Pilih menu untuk melanjutkan update:
        1. Berdasarkan NIS
        2. Kembali ke menu utama

        Pilih angka menu yang akan dipilih: """)
        if updateselect=='1':
            nis=int(input('Silahkan masukkan NIS yang akan di update: '))
            try:
                if nis=='':
                    print('Masukkan data dengan benar!')
            except ValueError:
                print('Mohon hanya input integer saja!')
            nisx = nis
            for x in range(len(allData)):
                if allData[x]['nis'] == nisx:
                    headernoindexPrint()
                    print('{}\t\t|{}\t\t|{}\t\t|{}\t\t|{}\t\t| {}'.format(allData[x]['kelas'],allData[x]['nis'],allData[x]['nama'],allData[x]['tugas'],allData[x]['UTS'],allData[x]['UAS']))
                    updatedata=input('''
                        Pilih data yang akan di ubah:

                        1. Kelas
                        2. Nama
                        3. Nilai Tugas
                        4. Nilai UTS
                        5. Nilai UAS
                        6. Kembali ke halaman update

                        Masukkan nomor yang akan di update: ''')
                    if updatedata=='1': # UPDATE KELAS
                        update_class=input('Masukkan update data "KELAS": ').capitalize()
                        try:
                            if update_class=='':
                                print('Masukkan data dengan benar!')
                        except ValueError:
                                print('Mohon hanya input string saja!')
                        updclopt=input('Yakin mengubah data kelas siswa NIS {} menjadi {}? (y/n): '.format(nisx,update_class)).lower()
                        if updclopt=='y':
                            for i in range(len(allData)):
                                allData[i].update({f'kelas': update_class})
                                print('Data telah di update!')
                                break
                        else:
                            print('Batal update. Anda akan diarahkan kembali ke halaman update.')
                            updateMain()
                    
                    elif updatedata=='2': # UPDATE NAMA
                        update_name=input('Masukkan update data "NAMA": ').capitalize()
                        try:
                            if update_name=='':
                                print('Masukkan data dengan benar!')
                                break
                        except ValueError:
                            print('Mohon hanya input string saja!')
                            break
                        updnaopt=input('Yakin mengubah data nama siswa NIS {} menjadi {}? (y/n): '.format(nisx,update_name))
                        if updnaopt=='y':
                            for i in range (len(allData)):
                                allData[i].update({f'nama': update_name})
                                print('Data telah di update!')
                                break
                        else:
                            print('Batal update. Anda akan diarahkan kembali ke halaman update.')
                            updateMain()

                    elif updatedata=='3': # UPDATE TUGAS
                        update_tugas=int(input('Masukkan update data "TUGAS": '))
                        try:
                            if update_tugas=='':
                                print('Masukkan data dengan benar!')
                                break
                        except ValueError:
                            print('Mohon hanya input integer saja!')
                            break
                        updtuopt=input('Yakin mengubah data nilai tugas siswa NIS {} menjadi {}? (y/n): '.format(nisx,update_tugas)).lower()
                        if updtuopt=='y':
                            for i in range (len(allData)):
                                allData[i].update({f'tugas': update_tugas})
                                print('Data telah di update!')
                                break
                        else:
                            print('Batal update. Anda akan diarahkan kembali ke halaman update.')
                            updateMain()

                    elif updatedata=='4': # UPDATE UTS
                        update_uts=input('Masukkan update data "UTS": ')
                        try:
                            if update_uts=='':
                                print('Masukkan data dengan benar!')
                        except ValueError:
                            print('Mohon hanya input integer saja!')
                        updutsopt=input('Yakin mengubah data nilai UTS siswa NIS {} menjadi {}? (y/n): '.format(nisx,update_uts)).lower()
                        if updutsopt=='y':
                            for i in range (len(allData)):
                                allData[i].update({f'UTS': update_uts})
                                print('Data telah di update!')
                                break
                        else:
                            print('Batal update. Anda akan diarahkan kembali ke halaman update.')
                            updateMain()

                    elif updateselect=='5': # UPDATE UAS
                        update_uas=input('Masukkan update data "UAS": ')
                        try:
                            if update_uas=='':
                                print('Masukkan data dengan benar!')
                        except ValueError:
                            print('Mohon hanya input integer saja!')
                        upduasopt=input('Yakin mengubah data nilai UAS siswa NIS {} menjadi {}? (y/n): '.format(nisx,update_uas)).lower()
                        if upduasopt=='y':
                            for i in range (len(allData)):
                                allData[i].update({f'UAS': update_uas})
                                print('Data telah di update!')
                                break
                    elif updateselect=='6':
                        updateMain()
                    else:
                        print('Menu yang anda pilih tidak tersedia. Anda akan diarahkan kembali ke halaman utama.')
                        mainPage()
        elif updateselect=='2':
            break
        else:
            print('Menu yang anda pilih tidak tersedia. Anda akan diarahkan kembali ke halaman utama.')
            mainPage()

# FUNCTION HAPUS DATA
def deleteMain():
    while (True):
        alldataPrint()
        deleteinput=int(input(f'\nMasukkan index siswa yang ingin dihapus:'))
        try:
            if deleteinput == '':
                print('Input yang anda masukkan salah, silahkan input kembali.')
        except ValueError:
                print('Input yang anda masukkan salah, silahkan input kembali.')
        else:
            del allData[deleteinput-1]
            alldataPrint()
            print('\nTerima kasih, data telah terhapus.')
            break

# FUNCTION HALAMAN UTAMA
def mainPage():
    while True:
        menu_select=input("""
            ====================================================
            Selamat datang di Database Siswa Sekolah Purwadhika!
            ====================================================

            Silahkan pilih menu:
            1. Menampilkan data siswa
            2. Menambah Data
            3. Update Data
            4. Menghapus Data
            5. Exit
        
            Silahkan masukkan angka menu yang dipilih: """)
        if (menu_select == '1'):
            readMain()
        elif (menu_select == '2'):
            createMain()
        elif (menu_select == '3'):
            updateMain()
        elif (menu_select == '4'):
            deleteMain()
        elif (menu_select == '5'):
            break
        else:
            print('Masukkan input yang sesuai!')
            mainPage()

mainPage()