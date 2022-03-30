# 942. DI String Match
Problem link: https://leetcode.com/problems/di-string-match/

## 문제 요약
[0, n] 범위의 모든 정수의 n + 1 정수 순열 `perm`은 길이 `n`인 문자열 `s`로 나타낼 수 있다.

- `s[i] == 'I' if perm[i] < perm[i + 1]`, and
- `s[i] == 'D' if perm[i] > perm[i + 1]`.


문자열 `s`가 주어지면 순열 `perm`을 재구성하고 반환한다. 유효한 순열 `perm`이 여러 개 있으면 그 중 하나를 반환하라.

예시 1:
- Input: s = "IDID"
- Output: [0,4,1,3,2]

예시를 해석해보면 `s = IDID` 가 출력 되었으므로, 
- s의 길이는 4이므로 `n = 4` 이다.
- 범위는 [0, n] 이므로 `[0, 4]`
- `perm[0]` 은 `perm[1]` 보다 작은 값이다. 
- `perm[1]` 은 `perm[2]` 보다 큰 값이다.   
- `perm[2]` 은 `perm[3]` 보다 작은 값이다.
- `perm[3]` 은 `perm[4]` 보다 큰 값이다.

Example 2:
- Input: s = "III"
- Output: [0,1,2,3]

Example 3:
- Input: s = "DDI"
- Output: [3,2,0,1]
 

Constraints:
- `1 <= s.length <= 105`
- `s[i]` is either 'I' or 'D'


# 기반 지식
##  Greedy algorithm

Greedy algorithm (탐욕 알고리즘)은 바로 눈앞의 이익만을 좇는 알고리즘을 말한다. 대부분의 경우에는 뛰어난 결과를 도출하지 못하지만, 드물게 최적해를 보장하는 경우도 있다. 그리디 알고리즘은 최적화 문제를 대상으로 한다. 최적해를 찾을 수 있으면 그것을 목표로 삼고, 찾기 어려운 경우에는 주어진 시간 내에 그런대로 괜찮은 해를 찾는 것을 목표로 삼는다. ₁

그리디 알고리즘이 잘 작동하는 문제들 ₂
- Greedy Choice Property(탐욕 선택 속성)을 갖고 있는 Optimal substructure(최적 부분 구조)인 문제들. 
    - Greedy Choice Property이란 앞의 선택이 이후 선택에 영향을 주지 않는 것.
    - Optimal substructure란 문제의 최적 해결 방법이 부분 문제에 대한 최적 해결 방법으로 구성되는 경우
- 위 두 조건을 만족하면 최적해를 찾을 수 있다. 하지만 그렇지 않더라도 그리디 알고리즘은 정답을 근사하게 찾는 용도로 활용 가능하며, 대부분의 경우 계산 속도가 빠르므로 매우 실용적이다. 

### 그리디 알고리즘이 잘 동작하는 예
- 다익스트라 알고리즘
- 허프만 코딩 알고리즘
- ID3 알고리즘 

### 그리디 알고리즘과 다이나믹 알고리즘의 차이 ₃
서로 풀 수 있는 문제의 성격이 다르며 알고리즘의 접근 방식이서로 반대방향으로 접근하는 구조이다. 
- 다이나믹 프로그래밍: 하위 문제에 대한 최적의 솔루션을 찾은 다음, 이 결과들을 결합한 정보에 입각해 전역 최적 솔루션에 대한 선택을 함.
- 그리디 알고리즘: 각 단계마다 로컬 최적해를 찾는 문제로 접근하여 문제를 더 작게 줄여나가는 형태.


# 문제풀이
## 내가 작성한 답
```python
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        nums = [i for i in range(len(S)+1)]
        ans = []
        for op in S:
            if op == 'I':
                ans += [nums[0]]
                nums = nums[1:]
            else:
                ans += [nums[-1]]
                nums = nums[:-1]
        return ans +[nums[0]]
```

## 해설



---
*참고문헌

₁. 문병로, 쉽게 배우는 알고리즘, p367

₂. 박상길, 파이썬 알고리즘 인터뷰, p585

₂. 박상길, 파이썬 알고리즘 인터뷰, p586
