# 常见算法模式参考

本文档总结了LeetCode中最常用的核心算法模式，帮助快速识别题目类型并选择合适的解决方案。

## 1. 双指针技巧

### 适用场景
- 数组或字符串的搜索、比较
- 需要同时追踪两个位置
- 优化暴力解法的嵌套循环

### 常见模式

#### 对撞指针
```python
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        left += 1
    else:
        right -= 1
```
**典型题目**：两数之和（有序数组）、回文判断、容器盛水

#### 快慢指针
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```
**典型题目**：链表环检测、链表中点

#### 同向双指针
```python
left = 0
for right in range(len(arr)):
    while condition:
        left += 1
```
**典型题目**：移除元素、移动零

---

## 2. 滑动窗口

### 适用场景
- 连续子数组/子字符串问题
- 需要维护一个动态区间

### 基本模板
```python
left = 0
for right in range(len(arr)):
    # 扩展窗口
    add_to_window(arr[right])
    
    # 收缩窗口
    while not valid_window():
        remove_from_window(arr[left])
        left += 1
    
    # 更新结果
    update_result()
```
**典型题目**：最小覆盖子串、无重复字符的最长子串

---

## 3. 动态规划

### 适用场景
- 求最优解（最大值、最小值、最长、最短）
- 问题可以分解为子问题
- 子问题存在重叠

### 基本模板
```python
# 1. 定义dp数组含义
dp = [0] * (n + 1)

# 2. 初始化base case
dp[0] = initial_value

# 3. 状态转移
for i in range(1, n + 1):
    dp[i] = function(dp[i-1], dp[i-2], ...)

# 4. 返回结果
return dp[n]
```

**典型题目**：爬楼梯、打家劫舍、零钱兑换、最长公共子序列

---

## 4. 回溯算法

### 适用场景
- 排列、组合、子集问题
- 需要穷举所有可能性

### 基本框架
```python
def backtrack(path, choices):
    if satisfy_condition:
        result.append(path[:])
        return
    
    for choice in choices:
        path.append(choice)
        backtrack(path, new_choices)
        path.pop()  # 回溯
```

**典型题目**：全排列、组合总和、子集、N皇后

---

## 5. 二分查找

### 适用场景
- 有序数组的搜索
- 答案在某个范围内，需要找最优值

### 基本模板
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**典型题目**：搜索插入位置、搜索旋转排序数组

---

## 6. DFS/BFS遍历

### 深度优先搜索（DFS）
```python
def dfs(node, visited):
    if not node or node in visited:
        return
    visited.add(node)
    process(node)
    for neighbor in node.neighbors:
        dfs(neighbor, visited)
```

### 广度优先搜索（BFS）
```python
from collections import deque

def bfs(start):
    queue = deque([start])
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        process(node)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**典型题目**：岛屿数量、二叉树层序遍历、最短路径

---

## 7. 贪心算法

### 适用场景
- 局部最优解能导致全局最优解
- 不需要回溯

### 基本思路
```python
def greedy(items):
    items.sort(key=lambda x: greedy_criterion(x))
    result = []
    for item in items:
        if can_select(item):
            result.append(item)
    return result
```

**典型题目**：跳跃游戏、分发饼干、区间调度

---

## 8. 哈希表优化

### 适用场景
- 需要快速查找、插入、删除
- 空间换时间
- 统计频率、去重

### 常见用法
```python
# 快速查找
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# 频率统计
from collections import Counter
freq = Counter(nums)
```

**典型题目**：两数之和、字母异位词分组、最长连续序列

---

## 9. 单调栈

### 适用场景
- 寻找下一个更大/更小元素
- 维护递增或递减序列

### 基本模板
```python
def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)
    
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)
    
    return result
```

**典型题目**：下一个更大元素、柱状图中最大的矩形、接雨水

---

## 10. 前缀和

### 适用场景
- 频繁查询子数组和
- 区间和问题

### 基本模板
```python
# 一维前缀和
prefix_sum = [0]
for num in nums:
    prefix_sum.append(prefix_sum[-1] + num)

# 查询区间[i, j]的和
range_sum = prefix_sum[j+1] - prefix_sum[i]

# 前缀和 + 哈希表（和为K的子数组）
def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    sum_count = {0: 1}
    
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in sum_count:
            count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count
```

**典型题目**：区域和检索、和为K的子数组

---

## 快速选择指南

### 根据数据结构
- **数组/字符串**：双指针、滑动窗口、前缀和、二分查找
- **链表**：快慢指针
- **树/图**：DFS、BFS

### 根据问题类型
- **最优解**：动态规划、贪心
- **穷举**：回溯、DFS
- **查找**：二分查找、哈希表
- **区间**：贪心、前缀和

### 常见模式识别
- 两数之和 → 哈希表
- 三数之和 → 双指针
- 子数组和 → 前缀和
- 最长子串 → 滑动窗口
- 岛屿问题 → DFS/BFS
- 排列组合 → 回溯
- 爬楼梯 → 动态规划

---

## 重要提示：灵活运用与自主思考

**以上算法模式仅作为参考工具，并非解题的唯一方式。**

在实际解题过程中，你应该：

1. **深入理解题意**：仔细分析题目的输入输出、约束条件和核心要求
2. **独立思考解法**：不要局限于已知模式，尝试从问题本质出发思考解决方案
3. **灵活组合运用**：很多题目需要组合多种算法思想，如"前缀和+哈希表"、"DFS+记忆化"等
4. **优化与创新**：即使使用常见模式，也要根据具体题目特点进行优化和调整
5. **举一反三**：理解算法背后的思想比记住模板更重要

**如果遇到无法用上述模式直接解决的题目：**
- 先尝试暴力解法，理解问题本质
- 分析时间/空间瓶颈在哪里
- 思考能否用数学方法、特殊性质或其他创新思路解决
- 考虑问题的变体和简化版本
- 从小规模测试用例中寻找规律

记住：**算法模式是辅助工具，独立思考和问题分析能力才是解题的核心。**
