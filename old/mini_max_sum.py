# https://www.hackerrank.com/challenges/mini-max-sum/problem

# 1
def minMaxSum(arr):
    arr.sort()
    total = sum(arr)
    print((total - arr[-1]), (total - arr[0]))
    
# 2
def minMaxSum(arr):
    print(sum(arr) - max(arr), sum(arr) - min(arr))
    
