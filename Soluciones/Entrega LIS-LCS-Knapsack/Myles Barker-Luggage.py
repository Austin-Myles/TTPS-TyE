import sys

def sack(elem, lim):
    n = len(elem) + 1
    m = lim + 1
    DP = []
    for _ in range(n):
        a = [0] * m
        DP.append(a) 
    
    for i in range(1, n):
        for j in range(1, m):
            if elem[i-1] > j:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max(
                    DP[i-1][j],
                    DP[i-1][j-elem[i-1]] + elem[i-1]
                )
    return DP[n-1][m-1]

cases = int(sys.stdin.readline().strip())
for _ in range(cases):
    lines = list(map(int, sys.stdin.readline().split()))
    limit = sum(lines) / 2

    if(limit.is_integer()): 
        if((sack(lines,int(limit))) == int(limit)):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

        