# Kode berikut adalah contoh cara melakukan proses pickle pada sebuah object dictionary dan menyimpannya pada sebuah file.

import pickle
contoh_dictionary = {1:"6", 2:"2", 3:"f"}
pickle_keluar = open("dict.pickle","wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()

# Kode berikut adalah contoh untuk mengekstraksi berkas pickle dan menaruhnya pada sebuah variabel.

import pickle
pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()

print(contohDictionary)