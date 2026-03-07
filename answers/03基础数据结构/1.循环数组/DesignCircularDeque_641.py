from typing import List

class MyCircularDeque:
    def __init__(self, k: int):
        self.data = [0] * k
        self.capacity = k
        self.front = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.front -= 1
        self.data[self.front] = value
        self.size += 1
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        insert_index = (self.front + self.size) % self.capacity
        self.data[insert_index] = value
        self.size += 1
        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front += 1
        self.size -= 1
        return True
    
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        self.size -= 1
        return True
    
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.data[self.front]
    
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.data[(self.front - 1 + self.size) % self.capacity]
    
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def isFull(self) -> bool:
        return self.size == self.capacity
