# 定义节点一般属性类
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# 定义单链表类
class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        curr = self.dummy_head.next

        for i in range(index):
            curr = curr.next
        
        return curr.val
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0, index) # 防止索引越界

        pred = self.dummy_head
        for j in range(index):
            pred = pred.next

        to_add = ListNode(val) # 定义要添加的节点

        to_add.next = pred.next
        pred.next = to_add

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        pred = self.dummy_head
        for k in range(index):
            pred = pred.next

        pred.next = pred.next.next
        
        self.size -= 1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
