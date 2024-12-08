from math import sqrt
import sys

#Time limit exceeded.

def factoriza(m):
    factores = {}
    for i in range(2, int(sqrt(m)) + 1):
        while m % i == 0:
            if i in factores:
                factores[i] += 1
            else:
                factores[i] = 1
            m //= i
    if m > 1:
        factores[m] = 1
    return factores

def divides_or_not(n, m):
    if m == 0:
        return (f"{m} does not divide {n}!")
    if m == 1:
        return (f"{m} divides {n}!")  
    
    factores = factoriza(m)
    for p, count in factores.items():
        potencia_p = 0
        potencia = p
        while potencia <= n:
            potencia_p += n // potencia
            potencia *= p
        if potencia_p < count:
            return (f"{m} does not divide {n}!")
        
    return (f"{m} divides {n}!")

def main():
    for line in sys.stdin:
        n, m = map(int, line.strip().split())
        print(divides_or_not(n, m))

if __name__ == "__main__":
    main()