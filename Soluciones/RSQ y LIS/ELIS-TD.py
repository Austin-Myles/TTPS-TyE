import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(" ")))

dp = [1] * n
prev = [-1] * n

def lis(nums, idx):
    if(dp[idx] != -1):
        return dp[idx]
    
    dp[idx] = 1
    prev[idx] = -1 

    for i in range(idx):
        if(nums[i] < nums[idx]) and (lis(nums, i) + 1 > dp[idx]):
            dp[idx] = lis(nums,i) + 1
            prev[idx] = i
    
    return dp[idx]

print(lis(nums, n-1))
