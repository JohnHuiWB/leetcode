# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def create(inputs):
        r = tmp = ListNode(0)
        if inputs:
            for i in inputs:
                tmp.next = ListNode(i)
                tmp = tmp.next
        return r.next

    def print_values(self):
        tmp = self
        l = []
        while tmp:
            l.append(tmp.val)
            tmp = tmp.next
        print(l)


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        o = r = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                r.next = ListNode(l1.val)
                l1 = l1.next
            else:
                r.next = ListNode(l2.val)
                l2 = l2.next
            r = r.next
        if l1:
            r.next = l1
        else:
            r.next = l2
        return o.next

    def mergeTwoLists2(self, l1, l2):
        if l1 and l2:
            if l1.val > l2.val: l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


if __name__ == '__main__':
    s = Solution()
    input_l1 = ListNode.create([1, 2, 4])
    input_l2 = ListNode.create([1, 3, 4])
    input_l1.print_values()
    input_l2.print_values()
    s.mergeTwoLists(input_l1, input_l2).print_values()
    s.mergeTwoLists2(input_l1, input_l2).print_values()
