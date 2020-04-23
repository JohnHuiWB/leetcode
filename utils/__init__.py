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

    def __str__(self):
        tmp = self
        l = []
        while tmp:
            l.append(tmp.val)
            tmp = tmp.next
        return l.__str__()

    def __lt__(self, other): #operator <
        return self.val < other.val