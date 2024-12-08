import sys

def calcular_criba(limite):
    criba = [True] * (limite + 1)
    criba[0], criba[1] = False, False

    for i in range(2, int(limite**0.5) + 1):
        if criba[i]:
            for j in range(i * i, limite + 1, i):
                criba[j] = False

    return criba

def goldbach(n, prime):
    for i in range(2, n):
        if prime[i] and prime[n - i]:
            return (i, n - i)
    return None  # Si no encuentra solución, aunque no debería suceder para números válidos

def main():
    output = []
    # Define un límite suficientemente grande para calcular todos los primos necesarios
    LIMITE = 10**7  
    primes = calcular_criba(LIMITE)

    for line in sys.stdin:
        aux = ""
        num = int(line.strip())
        if num < 8:
            output.append("Impossible.")
        else:
            if num % 2 == 0:
                aux = "2 2 "
                num -= 4
            else:
                aux = "2 3 "
                num -= 5
            
            result = goldbach(num, primes)
            if result:
                aux += " ".join(map(str, result)).strip()
                output.append(aux)
            else:
                output.append("Impossible.")  # Por si algo falla inesperadamente

    print("\n".join(output))

if __name__ == "__main__":
    main()
