import sys

#Tomado del apunte teorico de Numeros parte 2
def modular_exp_iter(x, y, n):
    res = 1
    while (y != 0):
        if y % 2 == 1:
            res = (res * x) % n
        x = (x * x) % n
        y //= 2
    return res

def main():
    output = [] # Lista para generar el output.
    datasets = int(sys.stdin.readline()) # Leemos la cantidad de datasets para utilizarlo dentro de un for loop.
    for _ in range(datasets):
        x, y, n = map(int, sys.stdin.readline().split()) # Obtenemos los terminos de x^y % n.
        output.append(str(modular_exp_iter(x, y, n)))
    sys.stdin.readline() # Para leer el 0.
    print("\n".join(output))

if __name__ == "__main__":
    main()