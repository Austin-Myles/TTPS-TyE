import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))

dp = [1] * n
prev = [-1] * n

def lis(nums):
    ans = 0

    for i in range(n):
        dp[i] = 1
        prev[i] = -1
    
        for j in range(i):
            if(nums[j]< nums[i]) and (dp[i] < dp[j] + 1):
                dp[i] = dp[j] + 1
                prev[i] = j
        
        if (dp[ans] < dp[i]):
            ans = i

    return ans

print(lis(nums))