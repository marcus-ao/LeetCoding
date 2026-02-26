from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        answer[0] = 1
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]

        right = 1
        for i in range(n-1, -1, -1):
            answer[i] = answer[i] * right

            right = right * nums[i]

        return answer
#####################以下为允许使用除法的解法#################
def productExceptSelfWithDivision(nums):
    # 计算总乘积
    total = 1
    zero_count = 0
    for num in nums:
        if num != 0:
            total *= num
        else:
            zero_count += 1
    
    # 根据0的个数分情况讨论
    """
    情况 1：没有 0 （zero_count == 0）
    这是最简单、最理想的情况。

    假设： nums = [2, 3, 4]
    此时： total = 24，zero_count = 0。
    代码走向： 执行 else: result.append(total // num)。
    结果： 24//2 = 12，24//3 = 8，24//4 = 6。完美。
    --------------------------------------------
    情况 2：刚好有 1 个 0 （zero_count == 1）
    这是最容易出错的情况。

    假设： nums = [2, 3, 0, 4]
    此时： total 排除了 0，只算了 2 * 3 * 4 = 24。zero_count = 1。
    代码走向： 执行 elif zero_count == 1: result.append(total if num == 0 else 0)。
    逻辑剖析：
    当你遍历到普通数字（比如 2）时：它“除了自身以外的乘积”里，必定包含那个唯一的 0。所以乘积一定是 0。
    当你遍历到那个唯一的 0 时：它“除了自身以外的乘积”，刚好就是其他所有数字的乘积！而这个纯净的乘积，刚好就是我们第一步小心翼翼算出来的 total（也就是 24）。
    结果： 遇到 2, 3, 4 时填入 0，遇到 0 时填入 24。输出 [0, 0, 24, 0]。完美。
    --------------------------------------------
    情况 3：有 2 个或以上的 0 （zero_count > 1）
    这其实是最省事的情况，属于“全军覆没”。

    假设： nums = [2, 0, 3, 0]
    代码走向： 执行 if zero_count > 1: result.append(0)。
    逻辑剖析： 既然数组里至少有两个 0。那么无论你把哪个数字遮住（当成“除了自身”），剩下的数字里绝对都还至少剩下一个 0。既然乘法式子里永远有 0，那所有的结果肯定全都是 0。
    结果： 无脑全部填入 0。输出 [0, 0, 0, 0]。完美。
    """
    result = []
    for num in nums:
        if zero_count > 1:
            result.append(0)
        elif zero_count == 1:
            result.append(total if num == 0 else 0)
        else:
            result.append(total // num)
    
    return result
