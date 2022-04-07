"""
There are two main issues that we should tackle, in order to design an efficient hashmap data structure:
1) hash function design and 2) collision handling.

1) hash function design and
해시 함수의 목적은 키 값을 저장 공간의 주소에 맵핑하는 것이다.
좋은 해시 함수는 값 충돌을 최소화 하고. 연산이 쉽고 빠르며, 해시 테이블 전체에 해시 값이 균일하게 분포해야 한다.
2) collision handling
본질적으로 해시 함수는 방대한 키 공간을 제한된 주소 공간으로 축소한다.
충돌은 불가피하기 때문에 충돌을 처리할 전략을 가지고 있는 것이 중요하다.
충돌이 얼마나 높은 확률로 발생할 수 있는 지는 '생일문제'를 참고하면 이해하기 쉽다.
"""


