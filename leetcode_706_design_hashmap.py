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


# put(key, value): 키, 값을 해시맵에 삽입. 이미 좋재하는 키일 경우 업데이트
# get(key, value): 키에 해당하는 값을 조회. 키가 존재하지 않으면 -1을 반환
# remove(key): 키에 해당하는 키, 값을 해시맵에서 삭제

# Separate Chaining 방식으로 구현
import collections

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)    # ListNode를 담게 될 기본 자료형 선언
        # collections.decaultdict: 존재하지 않는 키를 조회할 경우 자동으로 디폴트를 생성해줌

    def put(self, key: int, value: int) -> None:

        index = key % self.size

        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

