# Argument bersifat opsional
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()

if args.output:
    print("Halo, ini merupakan sebuah output dari panggildicoding.py")

# Argument Bersifat Wajib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
args = parser.parse_args()

print("Terima kasih telah menggunakan panggildicoding.py, " + args.nama)