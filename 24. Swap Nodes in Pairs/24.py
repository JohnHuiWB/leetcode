from utils import ListNode


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp_head = ListNode(0)
        tmp_head.next = head
        tmp = tmp_head
        while tmp.next and tmp.next.next:
            a, b = tmp.next, tmp.next.next
            tmp.next, a.next = b, b.next
            b.next = a
            tmp = tmp.next.next
        return tmp_head.next


if __name__ == '__main__':
    s = Solution()
    input_l = ListNode.create([1, 2, 3, 4])
    print(input_l)
    print(s.swapPairs(input_l))

