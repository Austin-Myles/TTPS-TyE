import sys

def ILYA(i, cadena):
    if(cadena[i] == cadena[i+1]):
        return 1
    else:
        return 0

try:  
    cadena = "0" + input()
    m = int(input())
    for _ in range(m):
        count = 0
        l, r = map(int, sys.stdin.readline().split(" "))
        for i in range(l, r):
            if(cadena[i] == cadena[i+1]):
                count += 1
        print(count)

except EOFError:
    pass
