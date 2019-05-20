# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(a):
    # Complete this function  
    sum1  = 0
    sum2  = 0
    for i in range(n):
        sum1 += int(a[i][i])
        sum2 += int(a[i][n-i-1])
    return abs(sum1 - sum2)
