import sys


def lis(elephants):

    ans = 0
    n = len(elephants)
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if(elephants[j][1] > elephants[i][1])and(dp[i] < dp[j]+1):
                dp[i] = dp[j] + 1
                prev[i] = j
    
    max_lis_len = max(dp)
    ans = dp.index(max_lis_len)

    elep_ret = []
    while ans != -1:
        elep_ret.append(elephants[ans][2])
        ans = prev[ans]
    
    print(max_lis_len)
    print(elep_ret)


elephants = []
index = 1
nums = sys.stdin.readline().strip()
while nums:
    elephant = list(map(int, nums.split()))
    elephant.append(index)
    elephants.append(elephant)
    index+=1
    nums = sys.stdin.readline().strip()

elephant_sort = sorted(elephants, key=lambda elephant: (elephant[0], -elephant[1]))

result = lis(elephant_sort)
