import sys

cases = int(sys.stdin.readline().strip())
sys.stdin.readline().strip()
for l in range(cases):

    heights = []
    while True:
        height = sys.stdin.readline().strip()
        if height == "":
            break
        heights.append(int(height))

    n = len(heights)
    dp = [1] * n
    prev = [-1] * n

    ans = 0
    for i in range(n):
        dp[i] = 1
        prev[i] = -1

        for j in range(i):
            if(heights[j] < heights[i]) and (dp[i] < dp[j] + 1):
                dp[i] = dp[j] + 1
                prev[i] = j
        
        if (dp[ans] < dp[i]):
            ans = i
    
    hits = []
    curr = ans
    while curr != -1:
        hits.append(heights[curr])
        curr = prev[curr]

    print(f"Max hits: {dp[ans]}")
    for i in range(len(hits) -1 , -1, -1):
        print(hits[i])
    if l < cases -1:
        print()