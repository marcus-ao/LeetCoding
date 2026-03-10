# 项目知识库 (PROJECT KNOWLEDGE BASE)

## 概览 (OVERVIEW)

这是一个AI辅助的LeetCode算法题目学习仓库。主要提供面向中文学习者的教育内容，并包含 Python 和 C++ 的代码实现。项目内置了一个自定义的 AI Skill (`leetcode-analyze-skill`)，用于自动生成题目分析文档。

## 目录结构 (STRUCTURE)

```
LeetCoding/
├── questions/              # LeetCode 题目原文（按学习模块/专题分类）
├── answers/                # 题目代码实现（与 questions 目录结构保持一致）
├── analysis/               # 详细的题目思路分析（与 questions 目录结构保持一致）
├── leetcode-analyze-skill/ # AI辅助分析 Skill 目录
├── GEMINI.md               # Gemini CLI 系统提示词
└── CONTRIBUTING.md         # 贡献指南
```

**命名规范:**
- 题目文件 (Questions): `{题号}. {题目名称}.md` (中文)
- 代码实现 (Answers): `{EnglishName}_{题号}.py`
- 分析文档 (Analysis): `{题号}-{EnglishName}-思路分析.md`

## 查找指南 (WHERE TO LOOK)

| 任务 | 位置 |
|------|----------|
| 添加新题目 | `questions/{模块}/` → `analysis/{模块}/` → `answers/{模块}/` |
| 使用 AI 分析题目 | `leetcode-analyze-skill/SKILL.md` |
| 查找算法模式 | `leetcode-analyze-skill/references/algorithm-patterns.md` |
| 查找相似题目 | `leetcode-analyze-skill/references/problem-categories.md` |
| 创建分析模板 | `leetcode-analyze-skill/assets/analysis-template.md` |

## 学习模块 (MODULES)

| 编号 | 模块 | 包含主题 |
|------|------|--------|
| 00 | 初生牛犊不怕虎 | 入门题 (两数之和、有效的括号 等) |
| 01 | 数组操作 | 前缀和, 差分数组, 二维数组 |
| 02 | 双指针技巧 | 数组双指针, 链表双指针, 滑动窗口, 二分搜索 |
| 03 | 基础数据结构 | 循环数组, 栈与队列, 哈希, 设计 |

## 约定规范 (CONVENTIONS)

### 代码风格 (Python)
```python
def solution(nums):
    """
    函数说明
    
    参数:
        nums: 输入数组
    
    返回:
        结果
    """
    # 清晰的变量命名
    result = []
    for num in nums:
        # 说明这一步在做什么
        result.append(num)
    return result
```

### 分析文档要求 (必须包含的10个章节)
1. 📋 题目信息
2. 📖 题目描述
3. 🤔 题目分析
4. 💡 解题思路 (暴力 → 优化)
5. 🎨 图解说明
6. ✏️ 代码框架填空
7. 💻 完整代码实现 (Python + C++)
8. ⚠️ 易错点提醒
9. 🔗 相似题目推荐
10. 📚 知识点总结

### Git 提交信息格式 (Commit Message Format)
- `Add: LeetCode {题号} - {题目名称}` - 新题目
- `Fix: {题号} - 修复代码错误` - Bug修复
- `Improve: {题号} - 改进解释` - 内容改进
- `Update: Skill文档更新` - Skill更新
- `Docs: 更新README` - 文档更新

## 反模式/禁止行为 (ANTI-PATTERNS)

### Python 严重错误
- **严禁** 使用 `[[0]*n]*n` 来初始化二维数组（会导致浅拷贝陷阱）
- **必须** 使用 `[[0] * n for _ in range(n)]` 来初始化二维数组

### 链表 严重错误
- **严禁** 在保存 `next_node = cur.next` 之前修改 `cur.next` 的指向
- **正确顺序**: 保存 (Save) → 断开 (Detach) → 重新连接 (Reattach)

### 循环数组 严重错误
- **严禁** 直接使用 `(index - 1) % capacity`，这在某些语言中会产生负数
- **必须** 使用 `(index - 1 + capacity) % capacity` 来处理负数索引问题

### 前缀和 严重错误
- **严禁** 在检查互补值（complement）是否存在之前，就将当前值更新到哈希表中
- **正确顺序**: 检查互补值 (Check complement) → 更新哈希表 (Update map)

### 代码填空练习 严重错误
- **严禁** 脱离完整代码单独编写填空练习的代码
- **必须** 先写出完整实现，然后 **从中** 挖空生成填空练习代码

### 算法模式误区
- **严禁** 将解题思路局限于参考文档中提供的 10 个模式
- **必须** 将模式视为工具，而不是不可违背的死规则

## 项目特色 (UNIQUE STYLES)

### 三重目录结构
`questions/` → `answers/` → `analysis/` 这三个目录结构完全镜像，对应了学习的核心工作流：阅读题目 → 尝试编写代码实现 → 学习详细的思路分析。

### 中文优先命名
由于目标受众为中文学习者，目录和题目文件名均优先使用中文。英文名称仅保留在分析文档的文件名中，以保持一定的国际兼容性。

### AI Skill 深度集成
仓库自带一个可移植的 AI Skill (`leetcode-analyze-skill/`)，专为 Claude Code、Gemini CLI 和 Codex 设计。调用方式："请使用leetcode-analyze-skill分析这道题目"

## 常用命令 (COMMANDS)

```bash
# 使用 AI 分析题目 (Claude Code 环境)
claude "请使用leetcode-analyze-skill分析 questions/.../1. 两数之和.md"

# 使用 AI 分析题目 (Gemini CLI 环境)
gemini "请使用leetcode-analyze-skill分析 questions/.../1. 两数之和.md"

# 运行 Python 解法代码
python answers/00初生牛犊不怕虎/TwoSum_1.py
```

## 备注 (NOTES)

- **无构建系统**: 这是一个纯文档/代码学习仓库，不需要配置包管理器（如 npm/pip）。
- **无 CI/CD**: 通过 PR 模板进行人工审查，无自动化测试流。
- **本地测试**: Python 文件中通常会包含 `if __name__ == "__main__":` 代码块用于快速本地测试。
- **Mermaid 绘图**: 分析文档中广泛支持并鼓励使用 Mermaid 生成图表。
- **虚拟头节点 (Dummy node)**: 链表操作时，**始终**考虑使用虚拟头节点以简化边界处理。
- **稳定划分 (Stable partition)**: 遇到链表/数组划分问题时，请注意题目是否要求保持元素的相对顺序。
