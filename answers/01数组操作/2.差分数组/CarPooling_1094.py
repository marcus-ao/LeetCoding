from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1001 # 虽然数组长度题目规定在0-1000，但是实际定义时要多一防止diff[1000]越界
        
        for num, left, right in trips:
            diff[left] += num
            diff[right] -= num

        current = 0

        for i in range(1, 1001):
            current += diff[i - 1]

            if current > capacity:
                return False
            
        return True
