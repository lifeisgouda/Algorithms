```python
def reverse(x):
    sign = 1
    if (x < 0):
        reverse = -1

    a = 0
    while x != 0:
        a = a * 10 + x % 10
        x = x // 10
    return sign * a
```



```python
def reverse(x):
    if x < 0:
        sign = -1
    else:
        sign = 1

    r = int(str(sign * x)[::-1])
    return (sign * r, 0)[r > 2 ** 31 - 1]
```





```python
# Get the s(sign), get the r(reversed) absolute integer, and return their product if r didn’t “overflow”.

# python 3.x
def reverse(x):
        sign = lambda x: x and (1, -1)[x < 0]
        r = int(str(sign(x)*x)[::-1])
        return (sign(x)*r, 0)[r > 2**31 - 1]
    
# python 2.x
def reverse(x):
    s = cmp(x, 0)             # 부호 결정.  cmp(x,y):x,y 비교
    r = int(`s*x`[::-1])      # 역순으로 출력
    return s*r * (r < 2**31)  # 부호 * 역순 * (역순 < 2의 31승)
```



x가 크면 양수, y가 크면 음수, 같으면 0을 반환

arr[A:B:C]의 의미는, index A 부터 index B 까지 C의 간격으로 배열을 만들어라.

```python
arr[::-2]    # 처음부터 끝까지 -2칸 간격으로 만듦( == 역순, 두 칸 간격으로 만듦)
```



