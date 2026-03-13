from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[nums[0]]
        slow = nums[0]

        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]

        finder = 0

        while fast != finder:
            fast = nums[fast]
            finder = nums[finder]

        return finder
