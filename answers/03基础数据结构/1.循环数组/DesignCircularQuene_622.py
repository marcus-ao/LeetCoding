from typing import List

class MyCircularQueue:
    def __init__(self, k: int):
        self.data = [0] * k
        self.capacity = k
        self.front = 0
        self.size = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.data[(self.front + self.size) % self.capacity] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.size -= 1
        self.front = (self.front + 1) % self.capacity
        return True
    
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.data[self.front]
    
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.data[(self.front -1 + self.size) % self.capacity]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity   
