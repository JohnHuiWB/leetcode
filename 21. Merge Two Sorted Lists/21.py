from utils import ListNode


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
    print(input_l1)
    print(input_l2)
    print(s.mergeTwoLists(input_l1, input_l2))
    print(s.mergeTwoLists2(input_l1, input_l2))
