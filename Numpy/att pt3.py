import numpy as np

# atividade 12

def absolute_split(array:np.ndarray, n:int):
    temp = np.abs(array)
    return np.array_split(temp, n)

att12 = np.random.randint(-9,10,(12))
print(att12)
print(absolute_split(att12,4))

print("\n")

# atividade 13

def count_positivenum(array:np.ndarray):
    positive = array[array > 0]
    return len(positive)

att13 = np.random.randint(-9,10,(10))
print(att13)
print(count_positivenum(att13))

print("\n")

# atividade 14

def divisible_by3(matrix:np.ndarray):
    row,column = np.where(matrix%3==0) # where(condição, elementos x, elementos y)
    return row,column

att14 = np.random.randint(1,10,(3,3))
print(att14, end='\n\n')
row,column = divisible_by3(att14)
print(f'Linha: {row}', f'Coluna: {column}')

print("\n")

# atividade 15

def look4negative(array:np.ndarray):
    return np.any(array < 0)

att15 = np.random.randint(-9,10,(4))
print(att15)
print(look4negative(att15))

print("\n")

# atividade 16

def popnegative(array:np.ndarray):
    return array[array >= 0]

att16 = np.random.randint(-9,10,(4))
print(att16)
print(popnegative(att16))

print("\n")

# atividade 17

def filterarray(array:np.ndarray,min:int,max:int):
    return array[(array >= min) & (array <= max)]

att17 = np.random.randint(-9,10,(10))
print(att17)
print(filterarray(att17, 4, 7))

print("\n")

# atividade 18

# where(condição, elementos x, elementos y)
def sortandremove(matrix:np.ndarray):
    temp = np.where(matrix%2==0,matrix,0) # removendo números ímpares
    temp = np.sort(temp, kind='quicksort') # ordenando os elementos da matriz
    return temp

att18 = np.random.randint(1,10,(3,3))
print(att18)
print(sortandremove(att18))

print("\n")

# atividade 19

def removeandsort(matrix:np.ndarray):
    temp = sortandremove(matrix)
    print(temp,end='\n\n')
    temp = np.unique(temp)
    return temp

att19 = np.random.randint(1,10,(5,5))
print(att19)
print(removeandsort(att19))

