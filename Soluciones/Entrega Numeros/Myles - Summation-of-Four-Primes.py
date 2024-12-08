import sys

def calcular_criba(limit):
    criba = [True] * (limit + 1) # Inicializamos la criba con True para todos los valores.
    criba[0], criba[1] = False, False # 0 y 1 no son primos.

    for i in range(2, int(limit**0.5) + 1):
        if criba[i]: # Si i es primo, entonces marcaremos a sus multiplos como no primos.
            for j in range(i * i, limit + 1, i):
                criba[j] = False

    return criba

def goldbach(n, prime): # Calculamos goldbach para 2 números habiendo restado previamente 4 o 5 en función si es par o impar.
    for i in range(2, n):
        if prime[i] and prime[n - i]:
            return (i, n - i)
    return None  # Si no encuentra solución, aunque no debería suceder para números válidos

def main():
    output = []
    limit = 10**7  # Definimos un limite grande para calcular todos los primos necesarios. En algunos tests de UDebug son numeros extremadamente grandes.
    primes = calcular_criba(limit) # Calculamos la criba de Eratóstenes hasta el limite definido.

    for line in sys.stdin:
        aux = ""
        num = int(line.strip())
        if num < 8: # Si el número es menor a 8, automaticamente lo descartamos.
            output.append("Impossible.")
        else:
            if num % 2 == 0: # Si es par, restamos 4 ya qué lo expresaremos con los 2 más 2 más otros dos números.
                aux = "2 2 "
                num -= 4
            else: # Similar para los impares, pero esta vez restamos 5.
                aux = "2 3 "
                num -= 5
            result = goldbach(num, primes)
            if result: # Si hay solución, la agregamos al output
                aux += " ".join(map(str, result)).strip()
                output.append(aux)
            else: # Si no hay solución, agregamos "Impossible."
                output.append("Impossible.") 

    print("\n".join(output))

if __name__ == "__main__":
    main()
