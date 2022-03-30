# https://www.hackerrank.com/challenges/staircase/problem

n = 6
for i in range(1, n+1):
    print(' '*(n-i)+'#'*i)

for i in range(1, n+1):
  print(('#'*i).rjust(n,' '))

for i in range(n):
    print('{:>{len}}'.format('#'*(i+1), len=n))
