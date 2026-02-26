from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        hashmap = {0: -1}
        prefix = 0
        max_length = 0

        for i, hour in enumerate(hours):
            prefix += (1 if hours[i] > 8 else -1)

            if prefix > 0:
                max_length = i + 1
            else:
                if prefix - 1 in hashmap:
                    length = i - hashmap[prefix - 1]
                    max_length = max(max_length, length)

            if prefix not in hashmap:
                hashmap[prefix] = i

        return max_length
