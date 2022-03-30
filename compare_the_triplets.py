# https://www.hackerrank.com/challenges/compare-the-triplets/problem

a = [1, 2, 3]
b = [3, 2, 1]

def compareTriplets(a, b):
    x = 0
    y = 0

    for i in range(len(a)):
        if a[i] == b[i]:
            x = x
            y = y
        elif a[i] < b[i]:
            x = x
            y += 1
        elif a[i] > b[i]:
            x += 1
            y = y

    return [x, y]

compareTriplets(a, b)


