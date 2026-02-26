from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            remainder = prefix % k

            if remainder in hashmap:
                if i - hashmap[remainder] >= 2:
                    return True
            else:
                hashmap[remainder] = i

        return False
