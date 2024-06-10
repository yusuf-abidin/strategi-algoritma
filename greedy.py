import pandas as pd
import time

start_time = time.time()

# Membaca data dari file CSV
df = pd.read_csv('database_calon_mahasiswa.csv')

# Menghitung total skor dengan bobot yang sudah ditentukan
df['Total Score'] = (df['Nilai Akademik'] * 0.5) + (df['Nilai Portofolio'] * 0.3) + (df['Essay'] * 0.2)

# Memilih mahasiswa dengan skor total di atas 80
selected_students = df[df['Total Score'] >= 80]

# Mengurutkan mahasiswa yang terpilih berdasarkan skor tertinggi
sorted_students = selected_students.sort_values(by='Total Score', ascending=False)

kapasitas = 3000
# Memilih mahasiswa berdasarkan kapasitas maksimum 
if len(sorted_students) > kapasitas:
    final_selection = sorted_students.head(kapasitas)
else:
    final_selection = sorted_students

# Menyimpan hasil ke dalam file Excel
final_selection.to_excel('greedy_mahasiswa_lolos.xlsx', index=False)

end_time = time.time()

# Hitung waktu eksekusi
execution_time = (end_time - start_time) * 1000

print(f"Berhasil menyimpan {kapasitas} mahasiswa teratas ke dalam 'greedy_mahasiswa_lolos.xlsx'.")
print(f"Waktu eksekusi: {execution_time:.2f} ms.")

