import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Número de argumentos incorretos")
        sys.exit(1)
    numero1 = float(sys.argv[1])
    numero2 = float(sys.argv[2])
    print(numero1 + numero2)
    print(sys.argv[0])
    sys.exit(0)