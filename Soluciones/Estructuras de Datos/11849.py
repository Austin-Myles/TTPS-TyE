import sys

while True:
    try:
        n, m = map(int, sys.stdin.readline().strip().split())

        if n == 0 and m == 0:
            break

        jack = set()
        for x in range(n):
            jack.add(int(sys.stdin.readline().strip()))
        
        cant = 0
        for x in range(m):
            if int(sys.stdin.readline().strip()) in jack:
                cant += 1
        
        print(cant)
    except EOFError:
        break