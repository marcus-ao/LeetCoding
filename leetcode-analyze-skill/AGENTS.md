# LeetCode 题目分析 Skill

AI驱动的LeetCode题目分析系统。通过5阶段工作流程生成全面的分析文档。

## 概览 (OVERVIEW)

本Skill自动化LeetCode题目分析，采用渐进式教学方法：暴力解法 → 优化解法，配合形象化类比和互动式代码填空练习。

## 目录结构 (STRUCTURE)
```
leetcode-analyze-skill/
├── SKILL.md                    # 核心工作流程 (5个阶段)
├── assets/
│   └── analysis-template.md    # 输出模板 (10个章节)
└── references/
    ├── algorithm-patterns.md   # 10个核心算法模式
    ├── analogy-examples.md     # 形象化类比库
    ├── code-filling-guide.md   # 代码填空设计指南
    ├── complexity-guide.md     # 复杂度分析指南
    └── problem-categories.md   # 题目分类
```

## 查找指南 (WHERE TO LOOK)

| 需求 | 文件 |
|------|------|
| 理解工作流程 | `SKILL.md` (第12-138行) |
| 创建分析文档 | `assets/analysis-template.md` |
| 查找算法模式 | `references/algorithm-patterns.md` |
| 创建类比 | `references/analogy-examples.md` |
| 设计代码填空 | `references/code-filling-guide.md` |
| 分析复杂度 | `references/complexity-guide.md` |
| 推荐相似题目 | `references/problem-categories.md` |

## 工作流程 (5个阶段)

### 阶段 1: 题目理解
- 提取: 编号, 标题, 描述, 示例, 约束
- 识别: 题目类型, 关键观察点

### 阶段 2: 解题思路分析
1. **形象化类比** (算法之前) - 查阅 `analogy-examples.md`
2. **暴力解法** - 描述直观解法, 分析复杂度
3. **优化解法** - 查阅 `algorithm-patterns.md`, 从瓶颈处推导优化

### 阶段 3: 图解说明
- Mermaid 图表或逐步追踪说明
- 避免 `"` 和 `()` 出现在 Mermaid 的 `[]` 中

### 阶段 4: 代码实现
1. **代码框架填空** - 查阅 `code-filling-guide.md`
2. **完整代码实现** - Python (主要) + C++ (辅助)

### 阶段 5: 补充信息
- **易错点提醒** - 边界条件, 常见错误
- **相似题目推荐** - 查阅 `problem-categories.md`

## 约定规范 (CONVENTIONS)

### 参考文档使用顺序
| 阶段 | 文档 | 用途 |
|-------|------|------|
| 2 | `analogy-examples.md` | 查找/创建类比 |
| 2 | `algorithm-patterns.md` | 匹配模式 (10个核心) |
| 2 | `complexity-guide.md` | 复杂度分析 |
| 4 | `code-filling-guide.md` | 设计填空 |
| 5 | `problem-categories.md` | 相似题目 |

### 输出命名
`{题目编号}-{EnglishName}-思路分析.md`
- 示例: `1-TwoSum-思路分析.md`
- 示例: `560-SubarraySumEqualsK-思路分析.md`

### 输出位置
`analysis/{模块路径}/{编号}-{名称}-思路分析.md`

## 反模式/禁止行为 (ANTI-PATTERNS)

### 关键: 代码填空一致性
- **严禁** 脱离完整实现单独编写填空代码
- **必须** 先设计完整代码，然后从中提取填空
- **原因**: 不一致会严重损害学习体验

### 关键: 算法模式限制
- **严禁** 将解题思路局限于 `algorithm-patterns.md` 中的10个模式
- **必须** 将模式视为参考工具，而不是唯一答案
- **原因**: 独立思考 > 模式匹配

### 类比质量
- **必须** 具体, 本质相关, 易于理解
- **必须** 包含: 场景, 对应关系, 核心理解

### 代码填空设计
- **保留**: 库导入, 函数定义, 基本结构
- **挖空**: 核心算法逻辑, 重要判断条件
- **提供**: 思考提示 (非直接答案)

## 项目特色 (UNIQUE STYLES)

### 渐进式教学
每篇分析遵循: 暴力 → 优化
- 展示暴力解法失败的原因 (瓶颈分析)
- 逐步推导优化方案

### 类比优先
复杂概念始终以生活类比开头:
```
🌟 形象化理解：[概念]
场景类比：[生活场景]
对应关系：[算法元素 = 生活元素]
核心理解：[一句话总结]
```

### 互动式学习
代码练习使用 `______` 标记并提供思考提示:
```python
# 🔹 填空1：初始化变量
# 提示：我们需要哪些变量来追踪状态？
______ = ______
```

## 常用命令 (COMMANDS)

通过AI助手调用本Skill:
```
"请使用leetcode-analyze-skill分析 questions/.../题目.md"
```

## 备注 (NOTES)

- **ACM模式**: 代码使用标准函数签名，非LeetCode类格式
- **双语言**: Python (主要，详细) + C++ (辅助，语法差异)
- **Mermaid限制**: 避免 `"` 和 `()` 出现在 `[]` 节点中
- **模板**: 需要10个章节 (见 `analysis-template.md`)
- **质量检查表**: 见 `GEMINI.md` 第177-187行
