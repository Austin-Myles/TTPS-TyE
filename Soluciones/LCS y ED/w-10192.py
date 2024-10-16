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
case = 1
while True:
    cadena1 = sys.stdin.readline().strip()
    cadena2 = sys.stdin.readline().strip()
    if cadena1 == "#" or cadena2 =="#":
        break
    else:
        print(f"Case #{case}: you can visit at most {LCS(cadena1,cadena2)} cities.")
    case+=1