#Haris Himawan
#202010225264
#TF3A6

import numpy as np
import sys


n = int(input('Masukkan jumlah variabel: '))


# membuat array berukuran n x n+1 dan menginisiasi
# menyimpan matriks augmented A / b
a = np.zeros((n,n+1))

# membuat array berukuran n dan menginisiasi
# vektor solusi
x = np.zeros(n)

# membaca koefisien matriks augmented
print('masukkan koefisien matriks augmented:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input(  'a['+ str(i)+']['+ str(j)+']='))

# implementasi eliminasi gauss jordan
for i in range(n):
    if a[i][i] == 0.0:
        sys.exit('divide by zero detected!')

    for j in range (n):
        if i != j:
            ratio = a[j][i]/a[i][i]

            for k in range (n+1):
                a[j][k] = a[j][k] - ratio * a[i][k]

# penentuan solusi
for i in range(n):
    x[i] = a[i][n]/a[i][i]

# menampilkan solusi
print('\nSolusi yang dibutuhkan: ')
for i in range(n):
    print('X%d = %0.6f' %(i,x[i]), end = '\t')