import numpy as np 

# atividade 1

att1 = np.arange(10, dtype='uint8')
print(att1)

print("\n")

# atividade 2

att2 = np.array([i for i in range(10)],dtype='uint8')
print(att2)

print("\n")

# atividade 3

att3 = np.array(([i for i in range(0, 3)],
                 [i for i in range(3, 6)],
                 [i for i in range(6, 9)]),dtype='uint8')

print(att3)

print("\n")

# atividade 3 - solução alternativa

att3s = np.arange(9).reshape((3,3))

print(att3s)

print("\n")

# atividade 4

att4 = np.array([1.4, 1.5, 2.5, 2.2, 5.6, 7.2, 9.2, 8.7, 5.9, 4.8],dtype='float32')
print(att4)
print(att4.itemsize) # 4bytes por elemento do array

print("\n")

# atividade 5

att5 = np.array([i for i in range(1, 21)],dtype='uint8')
print(att5)
print(att5.nbytes) # 1byte por elemento do array = 20bytes usados pelo array inteiro

print("\n")

# atividade 6

att6 = np.random.randint(1,10,(2,2))
print(att6,end='\n\n')
print(att6[0, 0], att6[1, 1]) # [linha, coluna]