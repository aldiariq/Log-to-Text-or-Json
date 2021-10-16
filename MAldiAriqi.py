# AssessmentTestSubmission
# Tools yang berfungsi untuk mengkonversi file log menjadi txt dan json
# yang ada pada system Linux menggunakan bahasa pemrograman Python3

# Deklarasi library
import time
import os
from os import path
import argparse
import json

# Method untuk menampilkan banner aplikasi
def tampilBanner():
    print("""
       d8888 888      888 d8b                  d8b                 888                       888                     888
      d88888 888      888 Y8P                  Y8P                 888                       888                     888
     d88P888 888      888                                          888                       888                     888
    d88P 888 888  .d88888 888  8888b.  888d888 888  .d88888        888      .d88b.   .d88b.  888888 .d88b.   .d88b.  888 .d8888b
   d88P  888 888 d88" 888 888     "88b 888P"   888 d88" 888        888     d88""88b d88P"88b 888   d88""88b d88""88b 888 88K
  d88P   888 888 888  888 888 .d888888 888     888 888  888 888888 888     888  888 888  888 888   888  888 888  888 888 "Y8888b.
 d8888888888 888 Y88b 888 888 888  888 888     888 Y88b 888        888     Y88..88P Y88b 888 Y88b. Y88..88P Y88..88P 888      X88
d88P     888 888  "Y88888 888 "Y888888 888     888  "Y88888        88888888 "Y88P"   "Y88888  "Y888 "Y88P"   "Y88P"  888  88888P'
                                                        888                              888
                                                        888                         Y8b d88P
                                                        888                          "Y88P"
""")
    print("Created By : M. Aldi Ariqi")

# Method untuk menampilkan pesan dialog
def tampilPesan(pesan):
    print("- " + pesan)

# Method untuk pengecekan akses root
def cekAksesroot():
    print("\nProses pengecekan akses root...")
    # Menampung uid pengguna saat script dijalankan
    uid = os.geteuid()
    # Kondisi jika uid bukan 0 (bukan root)
    if uid != 0:
        tampilPesan("Maaf, Untuk menjalankan script diperlukan akses root")
        exit()
    # Kondisi jika uid 0 (root)
    else:
        tampilPesan("Selamat, Script berhasil dijalankan")

# Method untuk pengecekan apakah direktori logfile valid atau tidak
def ceklokasiLog(lokasiLog):
    return path.exists(lokasiLog)

# Method untuk pengecekan apakah direktori output file valid atau tidak
def ceklokasiOutput(lokasiOutput):
    # Pengecekan apakah direktori dari file output ada atau tidak
    if path.exists(os.path.dirname(lokasiOutput)):
        # Pengecekan apakah file output dengan nama tersebut ada atau tidak
        if path.exists(lokasiOutput):
            return False
        else:
            return True
    else:
        return False

# Method untuk pengecekan apakah tipe konversi valid (text/json) atau tidak
def cektipeKonversi(tipe):
    # Pengecekan apakah tipe konversi dari argument berupa text
    if tipe == 'text':
        return True
    # Pengecekan apakah tipe konversi dari argument berupa json
    elif tipe == 'json':
        return True
    else:
        return False

# Method untuk menampilkan petunjuk penggunaan script
def tampilPentunjuk():
    print("\nPetunjuk Penggunaan")
    print("\n")
    print("Logfile dapat dikonversi dalam dua jenis file yaitu plaintext dan json")
    print("Pengguna cukup menambahkan flag '-t text' untuk plaintext dan '-t json' untuk json")
    print("Jika pengguna tidak menambahkan flag '-t', maka secara default logfile akan dikonversi menjadi plaintext")
    print("Contoh penggunaan : ")
    print("Konversi default (plaintext) : 'sudo python3 aldiariq-logtools.py /var/log/syslog'")
    print("Konversi ke plaintext : 'sudo python3 aldiariq-logtools.py /var/log/syslog -t text'")
    print("Konversi ke json : 'sudo python3 aldiariq-logtools.py /var/log/syslog -t json'")
    print("\n")
    print("Selain memilih jenis konversi, pengguna juga dapat menentukan lokasi hasil konversi")
    print("Pengguna cukup menambahkan flag '-o direktori/namafile.ekstensifile'")
    print("Jika pengguna tidak menambahkan flag '-o' maka hasil konversi akan disimpan pada direktori")
    print("tempat script dijalankan dengan nama output.formatfile")
    print("Contoh penggunaan : ")
    print("Konversi default (plaintext) : 'sudo python3 aldiariq-logtools.py /var/log/syslog -o /home/aldiariq/Data/log.txt'")
    print("Konversi ke plaintext : 'sudo python3 aldiariq-logtools.py /var/log/syslog -t text -o /home/aldiariq/Data/log.txt'")
    print("Konversi ke plaintext : 'sudo python3 aldiariq-logtools.py /var/log/syslog -t json -o /home/aldiariq/Data/log.json'")
    exit()

# Method untuk konversi log file
def konversiLog():
    # Inisialisasi dan konfigurasi argument parser
    argumentParser = argparse.ArgumentParser(add_help=False)
    argumentParser.add_argument("--help", "-h", action='store_true')
    argumentParser.add_argument("--tipe", "-t")
    argumentParser.add_argument("--output", "-o")
    argumentParser.add_argument("lokasilog", type=str, nargs='?')
    argument = argumentParser.parse_args()

    # Pengecekan apakah pengguna menggunakan flag -h
    if argument.help:
        # Menjalankan method tampil petunjuk
        tampilPentunjuk()
    
    print("\nProses Konversi Log File...")

    # Inisialisasi exsepsi proses konversi log file
    try:
        # Menampung lokasi log dari argument
        lokasilog = argument.lokasilog
        # Pengecekan apakah lokasi log valid
        if ceklokasiLog(lokasilog):
            # Pengecekan apakah pengguna menggunakan flag -t
            if argument.tipe:
                # Pengecekan apakah tipe konversi valid (text/json)
                if cektipeKonversi(argument.tipe):
                    tipekonversi = argument.tipe
                else:
                    tampilPesan("Pastikan tipe konversi text atau json")
                    exit()
            else:
                tipekonversi = 'text'

            # Pengecekan apakah pengguna menggunakan flag -o
            if argument.output:
                # Pengecekan apakah lokasi output valid
                if ceklokasiOutput(argument.output):
                    lokasioutput = argument.output
                else:
                    tampilPesan("Pastikan lokasi output benar dan file belum ada")
                    exit()
            else:
                # Pengecekan apakah tipe konversi text atau json
                # Jika konversi bertipe text maka format output file berupa .txt
                # Jika konversi bertipe json maka format output file berupa .json
                if tipekonversi == 'text':
                    formatfile = 'txt'
                else:
                    formatfile = 'json'
                lokasioutput = 'output.'+formatfile

            # Proses konversi log file
            # Statement jika tipe konversi adalah text
            if tipekonversi == 'text':
                # Proses pembacaan file log
                with open(lokasilog) as fileinput:
                    # Proses penulisan file output
                    with open(lokasioutput, "w") as fileoutput:
                        for kataperbaris in fileinput:
                            fileoutput.write(kataperbaris)
            
            # Statement jika tipe konversi adalah json
            if tipekonversi == 'json':
                # Inisialisasi json untuk menampung log
                jsonlog = {
                    "log": []
                }
                # Proses pembacaan file log
                with open(lokasilog) as fileinput:
                    # Proses pengisian jsonlog dengan isi file log
                    for kataperbaris in fileinput:
                        jsonlog["log"].append(kataperbaris.replace('\n', ''))
                # Proses penulisan file output
                with open(lokasioutput, 'w') as fileoutput:
                    json.dump(jsonlog, fileoutput, indent=4, sort_keys=True)

            tampilPesan("Proses konversi file log selesai")
        else:
            tampilPesan("Maaf, Dimohon untuk memeriksa apakah lokasi file log atau output benar")
    except Exception as e:
        tampilPesan("Maaf, Dimohon untuk memeriksa apakah lokasi log dan argumen penggunaan sudah benar")
        tampilPesan("Untuk melihat panduan silahkan menambahkan '-h' di akhiran argumen")
        tampilPesan("Contoh : 'sudo python3 aldiariq-logtools.py -h'")

# Method utama aplikasi
def methodUtama():
    # Menjalankan method tampilBanner
    tampilBanner()
    time.sleep(2)
    # Menjalankan method cek akses root
    cekAksesroot()
    time.sleep(2)
    # Menjalankan method baca log
    konversiLog()

# Menjalankan method utama
methodUtama()
