from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hash_map = {0: -1}
        prefix = 0
        max_length = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in hash_map:
                length = i - hash_map[prefix]
                max_length = max(length, max_length)
            else:
                hash_map[prefix] = i

        return max_length
