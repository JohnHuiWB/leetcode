from utils import ListNode


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        start = end = ListNode(0)
        tmp = head
        flag = True
        while head:
            for i in range(k):
                if not head:
                    flag = False
                    break
                head = head.next
            if not flag:
                break
            h = e = tmp
            while e.next != head:
                cur = h
                h = e.next
                e.next = h.next
                h.next = cur
            end.next = h
            end = e
            tmp = head

        return start.next


if __name__ == '__main__':
    s = Solution()
    input_l = ListNode.create([1, 2, 3, 4, 5])
    print(input_l)
    # print(s.reverseKGroup(input_l, 2))
    print(s.reverseKGroup(input_l, 3))
