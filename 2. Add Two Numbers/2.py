# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        r = result = ListNode(0)
        while l1 is not None and l2 is not None:
            sum = c + l1.val + l2.val
            c = sum // 10
            r.next = ListNode(sum % 10)
            r = r.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            sum = c + l1.val
            c = sum // 10
            r.next = ListNode(sum % 10)
            r = r.next
            l1 = l1.next

        while l2 is not None:
            sum = c + l2.val
            c = sum // 10
            r.next = ListNode(sum % 10)
            r = r.next
            l2 = l2.next

        if c > 0:
            r.next = ListNode(c)

        return result.next