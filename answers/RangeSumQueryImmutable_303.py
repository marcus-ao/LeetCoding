from typing import List
import sys

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.prefix[i+1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]

"""
假设系统以如下清晰的层级格式输入数据：

第一行：数组的长度 n

第二行：数组的具体元素 nums

第三行：查询的次数 q

接下来的 q 行：每行包含两个数字 left 和 right，代表每一次查询。
"""

if __name__ == "__main__":
    line_n = sys.stdin.readline().strip()
    if not line_n:
        exit()
    n = int(line_n)

    nums = list(map(int, sys.stdin.readline().split()))

    numarray = NumArray(nums)

    q = int(sys.stdin.readline().strip())

    for _ in range(q):
        left, right = map(int, sys.stdin.readline().split())
        result = numarray.sumRange(left, right)
        print(result)
