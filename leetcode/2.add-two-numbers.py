# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        p = l1
        q = l2
        cur = dummyHead
        carry = 0
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            sum = x + y + carry
            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        if carry > 0:
            cur.next = ListNode(carry)
        return dummyHead.next
