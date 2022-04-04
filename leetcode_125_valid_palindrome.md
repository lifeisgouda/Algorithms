# Valid Palindrome
## 팰린드롬이란?
- 오른쪽에서 왼쪽으로 읽으면서 같은 문자를 읽으면 된다.
- 예를 들어, "aba"는 팰린드롬이지만, "abca"는 팰린드롬이 아니다.

## 팰린드롬 여부 판별하기 풀이 1. 리스트로 변환
제약조건
- 대소문자 여부를 구분하지 않는다.
- 영문자, 숫자만 대상으로 한다.

제약 조건을 코드로 표현하면 다음과 같다.
```python
strs = []
for char in s:
    if char.isalnum():
        strs.append(char.lower())
```

Output
```python
['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']
```

팰린드롬 여부 판별하기
```python
while len(strs) > 1:
    if strs.pop(0) != strs.pop():
        return False
```
- pop(0)은 첫번째 문자를 제거하는 함수이다. pop()은 마지막 문자를 제거하는 함수이다.
- 첫번째 값고 마지막 값이 같은지 보고 일치하지 않으면 False를 반환한다. 모두 같으면 True를 반환한다.

```python
def isPalindrome(self, s:str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False
    return True
```

#### 외워두면 유용한 메서드
- `.isalnum()`: The isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
- `.isalpha()`: The isalpha() method returns True if all the characters are alphabet letters (a-z).
- `.isdigit()`: The isdigit() method returns True if all the characters are digits (0-9).
- `.islower()`: The islower() method returns True if all the characters are lowercase letters (a-z).
- `.isupper()`: The isupper() method returns True if all the characters are uppercase letters (A-Z).
- `.isspace()`: The isspace() method returns True if all the characters are whitespace characters (space, tab, newline, etc.).
- `.istitle()`: The istitle() method returns True if the string is a titlecased string and there is at least one character in the string.
- `.isnumeric()`: The isnumeric() method returns True if all the characters are numeric.
- `.isidentifier()`: The isidentifier() method returns True if the string is an identifier.
- `.isprintable()`: The isprintable() method returns True if all the characters are printable.
- `.isascii()`: The isascii() method returns True if all the characters are ASCII characters.
- `.isdecimal()`: The isdecimal() method returns True if all the characters are decimal digits (0-9).
- `.isdecimal()`: The isdecimal() method returns True if all the characters are decimal digits (0-9).
- `.isnumeric()`: The isnumeric() method returns True if all the characters are numeric.
- `.isidentifier()`: The isidentifier() method returns True if the string is an identifier.
- `.isprintable()`: The isprintable() method returns True if all the characters are printable.
- `.isascii()`: The isascii() method returns True if all the characters are ASCII characters.
- `.isalpha()`: The isalpha() method returns True if all the characters are alphabet letters (a-z).
- `.isdecimal()`: The isdecimal() method returns True if all the characters are decimal digits (0-9).
- `.isdigit()`: The isdigit() method returns True if all the characters are digits (0-9).
- `.islower()`: TheThe isalpha() method returns True if all the characters are alphabet letters (a-z).


## 팰린드롬 여부 판별하기 풀이 2: 데크 자료형을 이용한 최적화
Deque를 명시적으로 선언하면 속도를 높일 수 있다. 

```python
def isPalindrome(self, s:str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()
    
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return false
    
    return True
```


## 팰린드롬 여부 판별하기 풀이 3: 슬라이싱 사용
문자열 조작할 때 항상 슬라이싱을 우선으로 사용하는 것이 속도 개선에 유리하다.
```python
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규표현식으로 불필요한 문자 필터링. 영어, 숫자만 걸러내도록 함.
    s = re.sub('[^a-z0-9]', '', s)

    # 슬라이싱
    return s == s[::-1]  # [::-1]을 쓰면 뒤집을 수 있다.
```

---
참고자료
- 파이썬 알고리즘 인터뷰
- Leetcode solution