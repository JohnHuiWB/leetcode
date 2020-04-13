# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        records = [None] * (n + 1)
        orgin = head
        while head:
            records = records[1:] + [head]
            head = head.next
        if records[0]:
            records[0].next = records[0].next.next
            return orgin
        else:
            return orgin.next


if __name__ == '__main__':
    s = Solution()
    tmp = inputs = ListNode(1)
    tmp.next = ListNode(2)
    tmp = tmp.next
    tmp.next = ListNode(3)
    tmp = tmp.next
    tmp.next = ListNode(4)
    tmp = tmp.next
    tmp.next = ListNode(5)
    print(s.removeNthFromEnd(inputs, 2))
