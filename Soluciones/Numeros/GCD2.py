import sys

#Iterativo
def gcd_iter(u, v):
    while v:
        u, v = v, u % v
    return abs(u)

#Recursivo
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def main():
    cases = int(sys.stdin.readline())
    for _ in range(cases):
        a, b = map(int, sys.stdin.readline().split())
        print(gcd(a, b))

if __name__ == "__main__":
    main()