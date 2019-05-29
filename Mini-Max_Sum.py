# https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
    arr.sort()
    total = sum(arr)
    print((total - arr[-1]), (total - arr[0]))
    
