# https://www.hackerrank.com/challenges/plus-minus/problem

n = 6
arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
    negative = 0
    positive = 0
    zero = 0

    for i in range(n):
        if arr[i] > 0:
            positive += 1
        elif arr[i] == 0:
            zero += 1
        elif arr[i] < 0:
            negative += 1
        else:
            False

    posi = positive / n
    nega = negative / n
    ze = zero / n

    return print(posi, nega, ze, sep='\n')

plusMinus(arr)
