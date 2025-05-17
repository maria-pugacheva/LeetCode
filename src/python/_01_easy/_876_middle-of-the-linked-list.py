class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def addAtTail(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def traverse(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst


def returnMiddleOfLinkedListSolutionOne(head: Node) -> int:
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr[len(arr) // 2]


def returnMiddleOfLinkedListSolutionTwo(head: Node) -> int:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val


def testLinkedList():
    LL1 = LinkedList()
    LL1.addAtTail(Node(1))
    assert LL1.traverse() == [1]
    assert returnMiddleOfLinkedListSolutionOne(LL1.head) == 1
    assert returnMiddleOfLinkedListSolutionTwo(LL1.head) == 1

    LL2 = LinkedList()
    LL2.addAtTail(Node(1))
    LL2.addAtTail(Node(2))
    assert LL2.traverse() == [1, 2]
    assert returnMiddleOfLinkedListSolutionOne(LL2.head) == 2
    assert returnMiddleOfLinkedListSolutionTwo(LL2.head) == 2

    LL3 = LinkedList()
    LL3.addAtTail(Node(1))
    LL3.addAtTail(Node(3))
    LL3.addAtTail(Node(4))
    assert LL3.traverse() == [1, 3, 4]
    assert returnMiddleOfLinkedListSolutionOne(LL3.head) == 3
    assert returnMiddleOfLinkedListSolutionTwo(LL3.head) == 3

    LL4 = LinkedList()
    LL4.addAtTail(Node(1))
    LL4.addAtTail(Node(2))
    LL4.addAtTail(Node(5))
    LL4.addAtTail(Node(7))
    assert LL4.traverse() == [1, 2, 5, 7]
    assert returnMiddleOfLinkedListSolutionOne(LL4.head) == 5
    assert returnMiddleOfLinkedListSolutionTwo(LL4.head) == 5

    LL5 = LinkedList()
    LL5.addAtTail(Node(1))
    LL5.addAtTail(Node(2))
    LL5.addAtTail(Node(5))
    LL5.addAtTail(Node(7))
    LL5.addAtTail(Node(9))
    assert LL5.traverse() == [1, 2, 5, 7, 9]
    assert returnMiddleOfLinkedListSolutionOne(LL5.head) == 5
    assert returnMiddleOfLinkedListSolutionTwo(LL5.head) == 5

    print("All test cases passed!")


testLinkedList()
