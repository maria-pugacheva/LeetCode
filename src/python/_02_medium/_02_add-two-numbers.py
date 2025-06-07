class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addAtTail(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

class Solution:
    def traverse(self, LL: LinkedList):
        res = []
        node = LL.head
        while node:
            res.append(node.val)
            node = node.next
        return res

    def addTwoNumbers(self, ll1, ll2) -> LinkedList:
        ll = LinkedList()
        c = 0
        l1 = ll1.head
        l2 = ll2.head
        while l1 or l2 or c:
            n = c
            if l1:
                n += l1.val
                l1 = l1.next
            if l2:
                n += l2.val
                l2 = l2.next
            c = n // 10
            ll.addAtTail(n % 10)
        if c:
            ll.addAtTail(c)
        return ll


LL1 = LinkedList()
LL1.addAtTail(3)
LL1.addAtTail(2)
LL1.addAtTail(1)

LL2 = LinkedList()
LL2.addAtTail(9)
LL2.addAtTail(8)
LL2.addAtTail(5)

S = Solution()
res = S.addTwoNumbers(LL1, LL2)

assert S.traverse(LL1) == [3, 2, 1]
assert S.traverse(LL2) == [9, 8, 5]
assert S.traverse(res) == [2, 1, 7]

print('All test cases passed!')
