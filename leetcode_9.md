# [LeetCode] 9. Palindrome Number

> Determine whether an integer is a palindrome. Do this without extra space.
>
> 주어진 정수가 회문인지 판단하라. 공백은 고려하지 않는다.



## Approch

### 1. Palindrome

 회문이란 앞에서 부터 읽을 때와 뒤에서 부터 읽을 때가 같은 문장을 말한다

(ex) LEVEL, 12321, 다시합창합시다, 

여기서는 공백은 고려하지 않는다.



### 2. Idea

숫자가 주어질 때 맨 앞과 맨 뒤부터 순차적으로 비교하면 회문인지 알 수 있다.



### 3. Solution

음수인지 아닌지 판단하고, 음수가 아니면 x를 뒤에서 부터 읽은 값과 x가 동일한지 판단한다.

```python
class Solution:
    def isPalindrome(self, x):
        if x < 0 :
            False
        elif x[::-1] == x:
            return True
        else:
            return False
```