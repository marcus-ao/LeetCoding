# 303. 区域和检索 - 数组不可变

## 📋 题目信息
- **难度**：简单
- **标签**：设计、数组、前缀和
- **来源**：LeetCode

## 📖 题目描述

给定一个整数数组 `nums`，处理以下类型的多个查询:

1. 计算索引 `left` 和 `right` （包含 `left` 和 `right`）之间的 `nums` 元素的 **和** ，其中 `left <= right`

实现 `NumArray` 类：

* `NumArray(int[] nums)` 使用数组 `nums` 初始化对象
* `int sumRange(int left, int right)` 返回数组 `nums` 中索引 `left` 和 `right` 之间的元素的 **总和** ，包含 `left` 和 `right` 两点（也就是 `nums[left] + nums[left + 1] + ... + nums[right]` )

### 示例

**示例 1：**
```text
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
```

### 约束条件
- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`
- `0 <= left <= right < nums.length`
- 最多调用 `10^4` 次 `sumRange` 方法

---

## 🤔 题目分析

### 问题理解

我们需要设计一个数据结构，它接收一个整数数组，并能快速回答“从索引 left 到 right 所有元素的总和是多少”这个问题。

关键点：
- **数组不可变**：数组的内容在初始化后不会改变（Immutable）。
- **查询次数极多**：最多会调用 10^4 次查询请求。
- **时间要求高**：如果每次查询都重新遍历数组计算和，效率会很低，总操作次数可能达到 10^8 级别。

### 关键观察

既然数组不可变且查询次数多，这是典型的**空间换时间**场景。我们可以在类初始化的阶段（`__init__`）做一些预处理计算，从而将每次查询（`sumRange`）的时间大幅缩短到常数级别。

---

## 💡 解题思路

### 方法一：暴力解法

#### 思路说明

在 `sumRange` 方法中，直接使用一个循环，从 `left` 遍历到 `right`，把范围内的数字累加起来返回。

#### 算法步骤

1. 在 `__init__` 中直接保存传入的数组。
2. 每次调用 `sumRange(left, right)` 时，遍历 `nums[left]` 到 `nums[right]`。
3. 累加沿途的值并返回。

#### 复杂度分析

- **时间复杂度**：初始化 O(1)；每次查询 O(N)，其中 N 是查询区间的长度。如果有 Q 次查询，总时间复杂度为 O(N × Q)。
- **空间复杂度**：O(N) 用于保存数组。

#### 为什么需要优化

在极端情况下，数组长度为 10^4，查询调用次数也是 10^4。单次循环的时间复杂度 O(N) 累加起来会导致 10^8 次运算，很容易触发“超出时间限制”（Time Limit Exceeded）。我们需要一种 O(1) 的查询方法。

---

### 方法二：优化解法（前缀和）

#### 🌟 形象化理解（重点：优化的核心思想）

> **💡 在进入专业算法分析之前，先通过一个生活化的例子来理解优化思路的本质**

**场景类比**：银行账户余额

想象你在记录自己每天的**银行账户总余额**，而不是每天的具体收支。

**例如**：
如果你想知道“3月5日到3月10日这几天我的总收入是多少？”，
- **暴力做法**：把这5天每天的账单翻出来，一笔笔重新加起来。
- **聪明做法**：直接看3月10日的“总余额”，减去3月4日结束时的“总余额”。差值自然就是这几天的累计收支！

**对应关系**：
- **每天的具体收支** = 原数组中的每个元素 `nums[i]`
- **每天的总余额** = 预先计算好的前缀和数组 `prefix`
- **计算某几天的总收入** = 我们的区间求和查询 `sumRange(left, right)`
- **结束余额 - 开始前的余额** = `prefix[right + 1] - prefix[left]`

**核心理解**：
通过预先计算好从头开始的累加和，任何一个连续区间的总和都可以用两个累加和的差值“瞬间”得出！这就是**前缀和 (Prefix Sum)**。

**从类比到算法**：
现在让我们把这个生活化的思想转化为具体的算法...

---

#### 优化思路推导

**思考过程**：
1. 暴力解法的瓶颈在于每次查询都要重复遍历、累加中间的元素。
2. 我们可以通过预处理，把从索引 0 到每个位置 `i` 的总和提前算好。
3. 引入**前缀和**数组 `prefix`，定义 `prefix[i]` 表示前 `i` 个元素的和。
4. 那么 `nums[left]` 到 `nums[right]` 的和，就等于前 `right + 1` 个元素的和，减去前 `left` 个元素的和。

#### 算法步骤

1. **初始化前缀和数组**：创建一个长度为 `len(nums) + 1` 的数组 `prefix`，首位补 0。首位补 0 是为了方便计算从索引 0 开始的区间，不需要写额外的判断逻辑。
2. **预计算**：遍历传入的 `nums`，计算前缀和并依次存入：`prefix[i + 1] = prefix[i] + nums[i]`。
3. **极速查询**：对于任意的 `sumRange(left, right)` 查询，直接返回 `prefix[right + 1] - prefix[left]`。

#### 复杂度分析

- **时间复杂度**：
  - 初始化：O(N)，只在类实例化时遍历一次数组。
  - 查询：O(1)，无论区间多长，只做一次减法。
- **空间复杂度**：O(N)，我们需要创建一个长度为 N+1 的数组来存储前缀和。

#### 💭 回顾类比

- 生活中的【总余额】 对应 代码中的【前缀和数组 `prefix`】
- 生活中的【两个日期的余额做差】 对应 代码中的【`prefix[right + 1] - prefix[left]`】
- 这就是为什么区间求和查询能从线性的 O(N) 瞬间优化到常数级的 O(1) 的原因！

---

## 🎨 图解说明

### 执行过程示例

**示例输入**：`nums = [-2, 0, 3, -5, 2, -1]`

**执行步骤**：

**第一步：构建 `prefix` 数组**
构建一个长度为 `6 + 1 = 7` 的数组，第一位初始化为 0。

```text
原数组 nums:        -2      0      3     -5      2     -1
                  \   /  \   /  \   /  \   /  \   /  \   /
前缀和 prefix:  0  -> -2  -> -2  ->  1  -> -4  -> -2  -> -3
前缀和索引 :    0      1      2      3      4      5      6
```

**第二步：处理查询**
假设我们要执行 `sumRange(2, 5)`：
- 目标是求：`nums[2] + nums[3] + nums[4] + nums[5]` = `3 + (-5) + 2 + (-1)` = `-1`
- 利用前缀和直接相减：`prefix[5 + 1] - prefix[2]` = `prefix[6] - prefix[2]` = `(-3) - (-2)` = `-1`
瞬间计算完成！

---

## ✏️ 代码框架填空

> **💡 学习提示**：在查看完整代码之前，先尝试根据上面的算法步骤，自己思考并填写下面的空白处。这将帮助你从"不知道怎么开始"过渡到"能够独立实现关键逻辑"。

### Python填空版

```python
class NumArray:

    def __init__(self, nums: List[int]):
        # 🔹 填空1：初始化前缀和数组
        # 提示：为了方便计算，前缀和数组的长度应该比原数组多 1，且初始全为 0
        self.prefix = [0] * (______)
        
        # 🔹 填空2：计算并填充前缀和
        # 提示：遍历原数组，把累加的结果存入 prefix 中
        for i in range(len(nums)):
            # prefix 的后一位 等于 prefix 的前一位 加上 当前数字
            self.prefix[______] = self.prefix[______] + ______

    def sumRange(self, left: int, right: int) -> int:
        # 🔹 填空3：利用前缀和数组迅速返回结果
        # 提示：用包含right的“总余额” 减去 不包含left的“总余额”
        return self.prefix[______] - self.prefix[______]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```

### 填空提示详解

**填空1 - 初始化前缀和数组长度**
- 思考：原数组长度是 `len(nums)`，首位要额外加一个 0。因此前缀和的长度应该是多少？

**填空2 - 计算前缀和**
- 思考：`prefix` 第一个元素是 0，原数组的第一个元素 `nums[0]` 应该影响的是 `prefix[1]`。
- 如何表示累加？`prefix[i + 1]` 应该等于之前的和 `prefix[i]` 加上当前的数 `nums[i]`。

**填空3 - 利用前缀相减求区间和**
- 思考：我们要查 `left` 到 `right` 包含两端的和。对应的较大前缀和索引应该是 `right + 1`，被减去的较小前缀和索引应该是 `left`。

---

## 💻 完整代码实现

> **✅ 对照检查**：现在对比你的填空答案和下面的完整实现，看看思路是否一致。

### Python实现

```python
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        # 创建一个比原数组多一位的前缀和数组，第一位留作0
        self.prefix = [0] * (len(nums) + 1)
        
        # 预计算前缀和
        for i in range(len(nums)):
            # prefix[i+1] 代表着 nums 数组从第 0 项累加到第 i 项的总和
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # 要查询 [left, right] 的和，只要用 [0, right] 的和 减去 [0, left-1] 的和即可
        # 对应 prefix 数组索引就是 prefix[right + 1] - prefix[left]
        return self.prefix[right + 1] - self.prefix[left]

# 测试用例
if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    
    print(f"查询 [0, 2]: 预期 1, 实际 {obj.sumRange(0, 2)}")
    print(f"查询 [2, 5]: 预期 -1, 实际 {obj.sumRange(2, 5)}")
    print(f"查询 [0, 5]: 预期 -3, 实际 {obj.sumRange(0, 5)}")
```

**填空答案解析**：
- **填空1**：`len(nums) + 1` - 为方便计算，在开头加一个冗余的 0。
- **填空2**：`i + 1`, `i`, `nums[i]` - 状态转移方程，累加前面的和与当前的数。
- **填空3**：`right + 1`, `left` - 这是核心技巧。大索引 `right + 1` 包含了 `nums[right]`，而小索引 `left` 刚好是 `nums[left]` 前面的那部分的累加和。

---

### C++实现

```cpp
#include <vector>
using namespace std;

class NumArray {
private:
    // 成员变量用于存放前缀和
    vector<int> prefix;

public:
    NumArray(vector<int>& nums) {
        int n = nums.size();
        // 初始化前缀和数组大小为 n + 1，并将值全部赋为 0
        prefix.resize(n + 1, 0);
        
        // 依次计算前缀和
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + nums[i];
        }
    }
    
    int sumRange(int left, int right) {
        // 利用前缀和直接 O(1) 返回区间和
        return prefix[right + 1] - prefix[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
```

**与Python的主要差异**：
- C++在类中需显式定义私有成员变量 `vector<int> prefix;`。
- 在构造函数中使用 `resize` 方法为动态数组分配空间并赋初始值。

---

## ⚠️ 易错点提醒

### 1. 前缀和数组的长度与首位补 0

**易错点**：很容易直接建立和 `nums` 同样长度的 `prefix` 数组，导致求区间 `[0, right]` 的和时，无法用 `prefix[right] - prefix[-1]`（会引发数组越界或计算错误）。

**正确处理**：
```python
# 初始化多给 1 个位置，首位为 0
self.prefix = [0] * (len(nums) + 1)
```
有了开头的 `0`，`sumRange(0, right)` 就会自然转化为 `prefix[right + 1] - prefix[0]` = `prefix[right + 1] - 0`，逻辑统一，不用特殊写 `if left == 0:`。

### 2. 索引对应关系容易搞混

**错误写法**：
- `return prefix[right] - prefix[left - 1]`
- `return prefix[right] - prefix[left]`

**原因**：这由于我们给 `prefix` 开头多加了一个 0。因此 `prefix[1]` 存的才是 `nums[0]`。
**正确做法**：`nums` 的索引 `i` 对应到 `prefix` 中变成了 `i + 1`。因此要包含 `right`，上限是 `right + 1`；要排除 `left`，减去的下限是 `left - 1 + 1 = left`。

---

## 🔗 相似题目推荐

### 同类型题目

这些题目使用相同的前缀和技巧，只是维度或变体不同：

1. **[LeetCode 304] - 二维区域和检索 - 矩阵不可变** (Medium)
   - 相似点：这是本题的进阶二维版本，同样是利用前缀和思想，但在二维矩阵上建立二维前缀和。
   - 建议：掌握一维前缀和后，强烈推荐立刻去挑战这道二维版本。

2. **[LeetCode 560] - 和为 K 的子数组** (Medium)
   - 相似点：核心思想都是通过前缀和计算子数组和。
   - 进阶点：这道题需要将**前缀和**与**哈希表**结合使用（Two Sum的进阶变体），是面试中最常见的前缀和高频题。

### 相关知识点

本题涉及的核心知识点：

- **前缀和思想**：用于解决数组频繁进行区间求和查询的问题，是一种典型的空间换时间策略。
- **预处理与不可变性**：在数据结构设计题中，如果数据“不可变”（Immutable），通常都暗示应该在初始化时进行预处理。

---

## 📚 知识点总结

### 核心算法：前缀和 (Prefix Sum)

前缀和是一种非常重要且好用的数组预处理技巧。当你遇到**连续子数组的区间求和**问题时，首先应该条件反射般地想到前缀和。

### 解题模板

```python
# 前缀和通用模板
def build_prefix_sum(nums):
    # 1. 数组长度 + 1，首位赋 0
    prefix = [0] * (len(nums) + 1)
    
    # 2. 累加构建前缀和
    for i in range(len(nums)):
        prefix[i + 1] = prefix[i] + nums[i]
        
    return prefix

def query_range_sum(prefix, left, right):
    # 3. O(1) 查询区间和 [left, right]
    return prefix[right + 1] - prefix[left]
```

### 学习要点

1. **要点1**：理解空间换时间的思想。当查询极其频繁而数据不变时，预处理才是王道。
2. **要点2**：学会首位补 0 的小技巧（Dummy Head/Value 思想），这能帮我们免去烦人的 `left == 0` 的边界条件判断。
3. **要点3**：厘清原数组索引和前缀和数组索引之间的 `+1` 偏移对应关系。
4. **填空练习的价值**：通过填空，你应该掌握了如何独立推导前缀和的状态转移方程（累加）和区间求和公式（做差）。
