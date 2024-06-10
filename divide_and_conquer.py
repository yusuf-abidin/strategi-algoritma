import pandas as pd
import time

# Mulai menghitung waktu eksekusi
start_time = time.time() * 1000

# Fungsi untuk menghitung skor total
def calculate_total_score(df):
    df['Total Score'] = df['Nilai Akademik'] * 0.5 + df['Nilai Portofolio'] * 0.3 + df['Essay'] * 0.2
    return df

# Fungsi Divide and Conquer untuk memilih sebanyak kapasitas yang tersedia
def divide_and_conquer(df, n):
    if len(df) <= n:
        return df
    else:
        mid_index = len(df) // 2
        left_half = df.iloc[:mid_index]
        right_half = df.iloc[mid_index:]

        top_left = divide_and_conquer(left_half, n)
        top_right = divide_and_conquer(right_half, n)

        # Gabungkan dan urutkan kembali, ambil sebanyak kapasitas jika jumlah data melebihi kapasitas
        combined = pd.concat([top_left, top_right]).sort_values(by='Total Score', ascending=False).head(n)
        return combined

# Membaca data dari file CSV
df = pd.read_csv('database_calon_mahasiswa.csv')

kapasitas = 3000

# Menambahkan kolom 'Total Score' dan menghitungnya
df = calculate_total_score(df)

# Filter mahasiswa yang skor totalnya minimal 80
filtered_students = df[df['Total Score'] >= 80]


# Jika kurang dari kapasitas mahasiswa memenuhi kriteria, ambil semuanya
if len(filtered_students) < kapasitas:
    selected_students = filtered_students
else:
    # Gunakan Divide and Conquer untuk mendapatkan data mahasiswa sebanyak kapasitas yang ada
    selected_students = divide_and_conquer(filtered_students, kapasitas)

# Mengurutkan data mahasiswa teratas berdasarkan 'Total Score' dari yang tertinggi ke yang terendah
selected_students_sorted = selected_students.sort_values(by='Total Score', ascending=False)


# Menyimpan hasil ke dalam file Excel
selected_students_sorted.to_excel('divide_and_conquer_mahasiswa_lolos.xlsx', index=False)

# Akhiri waktu eksekusi
end_time = time.time() * 1000

# Hitung waktu eksekusi
execution_time = (end_time - start_time) 

print(f"Berhasil menyimpan {kapasitas} mahasiswa teratas ke dalam 'divide_and_conquer_mahasiswa_lolos.xlsx'.")
print(f"Waktu eksekusi: {execution_time:.2f} ms.")