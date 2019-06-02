# https://www.hackerrank.com/challenges/chocolate-in-box/problem

def chocolateInBox(arr):
    N = 0
    xor = 0
    for a in arr:
        xor ^= a
    for a in arr:
        if a^xor < a:
            N += 1
    
    return N
