import re  # Import modul regex

pola = '^a...v$'
string_tes = 'abyss'
hasil = re.match(pola, string_tes)

if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal.")

"""
Output:
Pencarian berhasil.
"""