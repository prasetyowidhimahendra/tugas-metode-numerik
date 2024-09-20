import numpy as np

# Mendefinisikan fungsi f(x) = x + e^x
def f(x):
    return x + np.exp(x)

# Metode Biseksi
def biseksi(f, a, b, toleransi=1e-6, max_iterasi=10):
    if f(a) * f(b) > 0:
        print("Fungsi tidak memiliki akar.")
        return None
    
    iterasi_count = 0
    while (b - a) / 2 > toleransi and iterasi_count < max_iterasi:
        c = (a + b) / 2
        if f(c) == 0:  # Jika nilai tengah adalah akar
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterasi_count += 1
    return (a + b) / 2

a, b = -1, 0

root_bisection = biseksi(f, a, b)
print(f"Akar (Hasil Metode Biseksi): {root_bisection}")

def regulafalsi(f, a, b, tolerance=1e-6, max_iteration=10):
    if f(a) * f(b) > 0:
        print("Fungsi tidak memiliki akar di interval tersebut.")
        return None
    
    iteration_count = 0
    c = a
    while abs(f(c)) > tolerance and iteration_count < max_iteration:
        # Menghitung nilai c
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteration_count += 1
    return c
import math 
def f(x):
    return x - math.exp(-x)

# Definisikan turunan f'(x)
def df(x):
    return 1 + math.exp(-x)

# Menjalankan Metode Newton Raphson
def newton_raphson(x0, Toleransi=1e-7, Max_iterasi=100):
    x = x0
    for i in range(Max_iterasi):
        fx = f(x)
        dfx = df(x)
        
        if dfx == 0:
            raise ValueError("Turunan f'(x) adalah nol. Metode gagal.")
        
        x_new = x - fx / dfx
        
        # Melakukan pengecekan konvergensi
        if abs(x_new - x) < Toleransi:
            return x_new
        
        x = x_new
    
    raise ValueError("Metode tidak konvergen dalam jumlah iterasi maksimum")

# Nilai awal x0
x0 = 0