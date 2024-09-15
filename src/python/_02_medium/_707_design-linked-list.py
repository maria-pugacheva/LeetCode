import unittest


# ---------------------------------------------------------------------
# Class Node
# ---------------------------------------------------------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# ---------------------------------------------------------------------
# Class LinkedList
# ---------------------------------------------------------------------
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        if index < 0 or not self.head:
            return -1
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        """Add a node of value val before the index-th node in the
        linked list. If index equals the length of the linked list, the
        node will be appended to the end of the linked list. If index is
        greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        prev = None
        for i in range(index):
            prev = curr
            if not curr:
                return
            curr = curr.next
        if prev:
            node = Node(val)
            node.next = curr
            prev.next = node
            if not node.next:
                self.tail = node
        else:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        prev = None
        if not curr:
            return
        if index == 0:
            self.head = curr.next
            if not self.head:
                self.tail = None
            return
        for i in range(index):
            prev = curr
            curr = curr.next
            if not curr:
                return
        prev.next = curr.next
        if not prev.next:
            self.tail = prev


# ---------------------------------------------------------------------
# Unit Tests
# ---------------------------------------------------------------------
class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linkedList = LinkedList()

    def testAddAtHead(self):
        self.linkedList.addAtHead(1)
        self.assertEqual(self.linkedList.get(0), 1)
        self.linkedList.addAtHead(2)
        self.assertEqual(self.linkedList.get(0), 2)
        self.assertEqual(self.linkedList.get(1), 1)

    def testAddAtTail(self):
        self.linkedList.addAtTail(1)
        self.assertEqual(self.linkedList.get(0), 1)
        self.linkedList.addAtTail(2)
        self.assertEqual(self.linkedList.get(1), 2)

    def testAddAtIndex(self):
        self.linkedList.addAtHead(1)
        self.linkedList.addAtTail(3)
        self.linkedList.addAtIndex(1, 2)  # LL: 1 -> 2 -> 3
        self.assertEqual(self.linkedList.get(1), 2)
        self.linkedList.addAtIndex(0, 0)  # LL: 0 -> 1 -> 2 -> 3
        self.assertEqual(self.linkedList.get(0), 0)
        self.linkedList.addAtIndex(4, 4)  # LL: 0 -> 1 -> 2 -> 3 -> 4
        self.assertEqual(self.linkedList.get(4), 4)
        self.linkedList.addAtIndex(10, 5)  # No change
        self.assertEqual(self.linkedList.get(5), -1)

    def testDeleteAtIndex(self):
        self.linkedList.addAtHead(1)
        self.linkedList.addAtTail(2)
        self.linkedList.addAtTail(3)  # LL: 1 -> 2 -> 3
        self.linkedList.deleteAtIndex(1)  # LL: 1 -> 3
        self.assertEqual(self.linkedList.get(1), 3)
        self.linkedList.deleteAtIndex(0)  # LL: 3
        self.assertEqual(self.linkedList.get(0), 3)
        self.linkedList.deleteAtIndex(0)  # LL becomes empty
        self.assertEqual(self.linkedList.get(0), -1)
        self.linkedList.deleteAtIndex(0)  # LL remains empty
        self.assertEqual(self.linkedList.get(0), -1)

    def testEdgeCases(self):
        # Testing on an empty list
        self.assertEqual(self.linkedList.get(0), -1)
        self.linkedList.deleteAtIndex(0)
        self.assertEqual(self.linkedList.get(0), -1)

        # Adding and removing a single element
        self.linkedList.addAtHead(10)
        self.assertEqual(self.linkedList.get(0), 10)
        self.linkedList.deleteAtIndex(0)
        self.assertEqual(self.linkedList.get(0), -1)


if __name__ == '__main__':
    unittest.main()
