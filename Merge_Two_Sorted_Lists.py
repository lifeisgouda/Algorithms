# https://leetcode.com/problems/merge-two-sorted-lists/

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


a = ListNode(1)
b = ListNode(2)
c = ListNode(4)

a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)

d.next = e
e.next = f

sol = Solution()
sol.mergeTwoLists(a, d)
