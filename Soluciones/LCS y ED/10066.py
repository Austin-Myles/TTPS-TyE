import sys

def LCS(s, t):
    n = len(s) + 1
    m = len(t) + 1
    memo = []
    for _ in range(n):
        a = [0] * m
        memo.append(a)
    for i in range(1, n):
        for j in range(1, m):
            if(s[i-1] == t[j-1]):
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    return memo[n-1][m-1]

twins = 1
while True:
    dims = list(map(int, sys.stdin.readline().split()))
    if dims[0] == 0 and dims[1] == 0:
        break
    else:
        lista1 = sys.stdin.readline().strip().split()
        lista2 = sys.stdin.readline().strip().split()
        print(f"Twin Towers #{twins}")
        print(f"Number of Tiles : {LCS(lista1,lista2)}\n")
        twins+=1

