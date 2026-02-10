# 时间/空间复杂度分析指南

本文档提供算法复杂度分析的系统方法，帮助准确评估算法的效率。

## 1. 时间复杂度基础

### 常见复杂度级别（从快到慢）

| 复杂度 | 名称 | 示例算法 | n=100时的操作数 |
|--------|------|----------|----------------|
| O(1) | 常数时间 | 数组访问、哈希表查找 | 1 |
| O(log n) | 对数时间 | 二分查找 | 7 |
| O(n) | 线性时间 | 遍历数组 | 100 |
| O(n log n) | 线性对数时间 | 归并排序、快速排序 | 700 |
| O(n²) | 平方时间 | 冒泡排序、选择排序 | 10,000 |
| O(n³) | 立方时间 | 三层嵌套循环 | 1,000,000 |
| O(2ⁿ) | 指数时间 | 递归求斐波那契 | 1.27×10³⁰ |
| O(n!) | 阶乘时间 | 全排列 | 9.3×10¹⁵⁷ |

### 复杂度比较

当 n = 1000 时：
- O(log n) ≈ 10 次操作
- O(n) = 1,000 次操作
- O(n log n) ≈ 10,000 次操作
- O(n²) = 1,000,000 次操作
- O(2ⁿ) = 无法计算（太大）

**经验法则**：
- n ≤ 10: O(n!) 可接受
- n ≤ 20: O(2ⁿ) 可接受
- n ≤ 500: O(n³) 可接受
- n ≤ 5000: O(n²) 可接受
- n ≤ 10⁶: O(n log n) 可接受
- n ≤ 10⁸: O(n) 可接受
- n > 10⁸: 需要 O(log n) 或 O(1)

---

## 2. 时间复杂度分析方法

### 2.1 单层循环

```python
# O(n)
for i in range(n):
    # O(1) 操作
    print(i)
```

**分析**：循环执行 n 次，每次 O(1) → 总时间 O(n)

### 2.2 嵌套循环

```python
# O(n²)
for i in range(n):
    for j in range(n):
        # O(1) 操作
        print(i, j)
```

**分析**：外层循环 n 次，内层循环 n 次 → n × n = O(n²)

```python
# O(n²) - 虽然内层循环次数递减
for i in range(n):
    for j in range(i, n):
        # O(1) 操作
        print(i, j)
```

**分析**：总操作数 = n + (n-1) + (n-2) + ... + 1 = n(n+1)/2 ≈ O(n²)

### 2.3 对数复杂度

```python
# O(log n)
i = 1
while i < n:
    i *= 2
    # O(1) 操作
```

**分析**：i 的值为 1, 2, 4, 8, ..., 2^k，当 2^k = n 时停止，k = log₂n → O(log n)

```python
# O(log n) - 二分查找
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**分析**：每次循环将搜索范围减半 → O(log n)

### 2.4 线性对数复杂度

```python
# O(n log n)
for i in range(n):
    j = 1
    while j < n:
        j *= 2
        # O(1) 操作
```

**分析**：外层 O(n)，内层 O(log n) → O(n log n)

**典型例子**：归并排序、快速排序、堆排序

---

## 3. 递归复杂度分析

### 3.1 递归树方法

#### 示例1：斐波那契数列（低效版本）

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
```

**递归树**：
```
                fib(5)
              /        \
          fib(4)      fib(3)
         /     \      /     \
     fib(3)  fib(2) fib(2) fib(1)
     /   \    /  \   /  \
  fib(2) fib(1) ...
```

**分析**：
- 树的高度：n
- 每层节点数：约 2^层数
- 总节点数：约 2^n
- **时间复杂度：O(2ⁿ)**

#### 示例2：二分递归

```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, right)
    else:
        return binary_search_recursive(arr, target, left, mid-1)
```

**分析**：
- 每次递归将问题规模减半
- 递归深度：log n
- **时间复杂度：O(log n)**

### 3.2 主定理（Master Theorem）

对于递归关系：T(n) = aT(n/b) + f(n)

其中：
- a：子问题数量
- n/b：子问题规模
- f(n)：合并子问题的时间

**三种情况**：

1. 如果 f(n) = O(n^(log_b(a) - ε))，则 T(n) = O(n^log_b(a))
2. 如果 f(n) = O(n^log_b(a))，则 T(n) = O(n^log_b(a) × log n)
3. 如果 f(n) = O(n^(log_b(a) + ε))，则 T(n) = O(f(n))

**示例**：

```python
# 归并排序：T(n) = 2T(n/2) + O(n)
# a=2, b=2, f(n)=O(n)
# log_b(a) = log_2(2) = 1
# f(n) = O(n^1) → 情况2
# 结果：O(n log n)
```

---

## 4. 空间复杂度分析

### 4.1 基本原则

空间复杂度考虑：
1. **输入空间**：通常不计入（题目给定）
2. **辅助空间**：算法使用的额外空间
3. **输出空间**：有时计入，视题目要求

### 4.2 常见情况

#### O(1) 空间
```python
# 只使用固定数量的变量
def sum_array(arr):
    total = 0  # O(1)
    for num in arr:
        total += num
    return total
```

#### O(n) 空间
```python
# 使用额外数组
def copy_array(arr):
    result = []  # O(n)
    for num in arr:
        result.append(num)
    return result
```

#### O(n²) 空间
```python
# 使用二维数组
def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]  # O(n²)
    return matrix
```

### 4.3 递归的空间复杂度

递归调用会使用调用栈空间：

```python
# O(n) 空间 - 递归深度为n
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```

**分析**：递归深度 = n，每层占用 O(1) 空间 → 总空间 O(n)

```python
# O(log n) 空间 - 递归深度为log n
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, right)
    else:
        return binary_search_recursive(arr, target, left, mid-1)
```

**分析**：递归深度 = log n → 空间 O(log n)

---

## 5. 常见数据结构的复杂度

### 数组（Array）
| 操作 | 时间复杂度 |
|------|-----------|
| 访问 | O(1) |
| 搜索 | O(n) |
| 插入（末尾） | O(1) |
| 插入（中间） | O(n) |
| 删除（末尾） | O(1) |
| 删除（中间） | O(n) |

### 链表（Linked List）
| 操作 | 时间复杂度 |
|------|-----------|
| 访问 | O(n) |
| 搜索 | O(n) |
| 插入（头部） | O(1) |
| 插入（尾部） | O(n) 或 O(1)* |
| 删除（头部） | O(1) |
| 删除（已知节点） | O(1) |

*如果维护尾指针则为 O(1)

### 哈希表（Hash Table）
| 操作 | 平均时间 | 最坏时间 |
|------|---------|---------|
| 查找 | O(1) | O(n) |
| 插入 | O(1) | O(n) |
| 删除 | O(1) | O(n) |

### 二叉搜索树（BST）
| 操作 | 平均时间 | 最坏时间 |
|------|---------|---------|
| 查找 | O(log n) | O(n) |
| 插入 | O(log n) | O(n) |
| 删除 | O(log n) | O(n) |

### 堆（Heap）
| 操作 | 时间复杂度 |
|------|-----------|
| 查找最小/最大 | O(1) |
| 插入 | O(log n) |
| 删除最小/最大 | O(log n) |
| 建堆 | O(n) |

---

## 6. 复杂度分析常见陷阱

### 陷阱1：忽略隐藏的循环

```python
# 看起来是O(n)，实际是O(n²)
for i in range(n):
    s = s + str(i)  # 字符串拼接是O(n)操作！
```

**正确分析**：字符串拼接需要创建新字符串，复制所有字符 → O(n²)

**优化**：使用列表
```python
# O(n)
result = []
for i in range(n):
    result.append(str(i))
s = ''.join(result)
```

### 陷阱2：忽略排序的复杂度

```python
# 看起来是O(n)，实际是O(n log n)
def process(arr):
    arr.sort()  # O(n log n)
    for num in arr:  # O(n)
        print(num)
```

**正确分析**：O(n log n) + O(n) = O(n log n)

### 陷阱3：递归中的重复计算

```python
# 看起来是O(n)，实际是O(2ⁿ)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)  # 大量重复计算
```

**优化**：使用记忆化
```python
# O(n)
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

### 陷阱4：均摊分析

```python
# 动态数组的append操作
# 单次操作：通常O(1)，偶尔O(n)（扩容时）
# 均摊复杂度：O(1)
arr = []
for i in range(n):
    arr.append(i)  # 均摊O(1)
```

---

## 7. 复杂度优化策略

### 策略1：空间换时间
- 使用哈希表：O(n²) → O(n)
- 使用记忆化：O(2ⁿ) → O(n)

### 策略2：预处理
- 前缀和：多次查询区间和 O(n) → O(1)
- 排序：多次查找 O(n) → O(log n)

### 策略3：双指针
- 嵌套循环：O(n²) → O(n)

### 策略4：分治
- 暴力枚举：O(n²) → O(n log n)

### 策略5：贪心
- 动态规划：O(n²) → O(n)

---

## 8. 实战分析示例

### 示例：两数之和

#### 暴力解法
```python
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
```
- **时间复杂度**：O(n²) - 两层循环
- **空间复杂度**：O(1) - 只用了常数变量

#### 哈希表优化
```python
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```
- **时间复杂度**：O(n) - 一次遍历
- **空间复杂度**：O(n) - 哈希表存储

**优化总结**：用 O(n) 空间换取时间从 O(n²) 降到 O(n)

---

## 9. 快速判断技巧

1. **看循环层数**：单层→O(n)，双层→O(n²)
2. **看是否减半**：每次减半→O(log n)
3. **看递归分支**：每次分两支→可能O(2ⁿ)
4. **看是否排序**：有排序→至少O(n log n)
5. **看数据结构**：哈希表→O(1)查找，数组→O(n)查找
