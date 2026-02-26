from typing import List

class Solution:
    def getModifiedArray(self, n: int, updates: List[List[int]]) -> List[int]:
        diff = [0] * n

        for start, end, inc in updates:
            diff[start] += inc

            if end < n - 1:
                diff[end + 1] -= inc
        
        for i in range(1, n):
            diff[i] += diff[i - 1]

        return diff
