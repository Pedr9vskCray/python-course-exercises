import numpy as np

# atividade 7

att7 = np.random.randint(5,21,(3,3))
print(att7,end='\n\n')
print(att7[:, 0])
print(att7[2, :])

print("\n")

# atividade 8

att8 = np.random.randint(1,10,(3,3))
print(att8, end='\n\n')
for line in att8:
    print(np.sum(line))

print("\n")

# atividade 9

att9 = np.array([i for i in range(0,101,2)],dtype='uint8')
print(att9)

print("\n")

# atividade 10

att10 = np.random.randint(1,10,(4,9))
print(att10, end='\n\n')
print(att10.reshape(36), end='\n\n')
print(att10.reshape((6,6)), end='\n\n')

print("\n")

# atividade 11

def concatena_array(array1:np.ndarray, array2:np.ndarray, array3:np.ndarray):
    if (array1.shape != array2.shape) or (array1.shape != array3.shape):
        raise ValueError("Um dos arrays tem um tamanho diferente dos outros.")
    else:
        return np.concatenate((array1,array2,array3), axis=0)

teste1 = np.random.randint(1,10,(2,2))
teste2 = np.random.randint(1,10,(2,2))
teste3 = np.random.randint(1,10,(2,2))
diferente = np.random.randint(1,10,(3,3))

print(teste1, end='\n\n')
print(teste2, end='\n\n')
print(teste3, end='\n\n')
print(concatena_array(teste1, teste2, teste3), end='\n\n')