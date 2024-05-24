import pandas as pd

# membuat data frame dari dictionary
data = {
    'nama': ['John', 'Jane', 'Bob', 'Alice'],
    'usia': [25, 30, 22, 28],
    'Pekerjaan': ['Enginner', 'Teacher', 'Designer', 'Doctor']
}

df = pd.DataFrame(data)

# Menampilkan DataFrame
print(df)