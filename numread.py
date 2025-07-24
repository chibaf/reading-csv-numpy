import numpy as np
#with open('./LR5-SSR_2025-07-19_H11_M07_S01.csv',delimiter=',') as f:
print(np.loadtxt('./LR5-SSR_2025-07-19_H11_M07_S01.csv', delimiter=',', dtype='float',skiprows=1, usecols=[1,2,3,4,5,6,7,8,9,10,11]))
#  print(f.read())