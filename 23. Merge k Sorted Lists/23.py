from utils import ListNode


class Solution(object):
    def mergeKLists(self, lists):
        """
        用优先队列优化方法
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # For python 2
        # from queue import PriorityQueue

        # For python 3
        from queue import PriorityQueue

        head = cur = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            cur.next = ListNode(val)
            cur = cur.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next

    def mergeKLists2(self, lists):
        """
        分治
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def mergeTwoLists(l1, l2):
            if l1 and l2:
                if l1.val > l2.val: l1, l2 = l2, l1
                l1.next = mergeTwoLists(l1.next, l2)
            return l1 or l2

        amount = len(lists)
        new_lists = []
        while amount > 1:
            for i in range(0, amount // 2):
                new_lists.append(mergeTwoLists(lists[i * 2], lists[i * 2 + 1]))
            if amount % 2:
                new_lists.append(lists[-1])
            lists = new_lists
            new_lists = []
            amount = len(lists)
        return lists[0] if amount > 0 else None


if __name__ == '__main__':
    s = Solution()
    input_l1 = ListNode.create([1, 4, 5])
    input_l2 = ListNode.create([1, 3, 4])
    input_l3 = ListNode.create([2, 6])
    print(input_l1)
    print(input_l2)
    print(input_l3)
    print(s.mergeKLists([input_l1, input_l2, input_l3]))
    print(s.mergeKLists2([input_l1, input_l2, input_l3]))
