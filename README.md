# LeetCoding - LeetCode算法题目学习仓库

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

一个系统化的LeetCode算法题目学习仓库，包含题目原文、详细的思路分析文档以及一个强大的AI辅助分析Skill。

## 📁 项目结构

```
LeetCoding/
├── questions/              # LeetCode题目原文
│   ├── 1. 两数之和.md
│   ├── 20. 有效的括号.md
│   ├── 136. 只出现一次的数字.md
│   └── ...
├── analysis/               # 题目详细分析文档
│   ├── 1-TwoSum-思路分析.md
│   ├── 20-ValidParentheses-思路分析.md
│   ├── 136-SingleNumber-思路分析.md
│   └── ...
├── leetcode-analyze-skill/ # AI辅助分析Skill
│   ├── SKILL.md           # Skill主文档
│   ├── assets/            # 模板资源
│   └── references/        # 参考文档
├── GEMINI.md              # GeminiCLI系统提示词
└── README.md              # 本文件
```

## ✨ 特色功能

### 1. 系统化的题目分析

每道题目的分析文档都包含：

- 📋 **题目信息**：难度、标签、来源
- 📖 **题目描述**：完整的题目要求和示例
- 🤔 **题目分析**：从零开始的思路理解
- 💡 **解题思路**：暴力解法 → 优化解法的完整推导
- 🌟 **形象化类比**：用生活化例子降低理解难度
- 🎨 **图解说明**：可视化关键步骤
- ✏️ **代码框架填空**：互动式学习，关键代码挖空
- 💻 **完整代码实现**：Python + C++ 双语言实现
- ⚠️ **易错点提醒**：边界条件、常见错误、调试技巧
- 🔗 **相似题目推荐**：举一反三，系统化学习

### 2. AI辅助分析Skill

本仓库包含一个专业的LeetCode题目分析Skill，可以配合AI助手使用：

- **渐进式讲解**：从简单到复杂，从暴力到优化
- **形象化类比**：将抽象算法概念转化为生活场景
- **互动式填空**：通过代码填空练习加深理解
- **完整参考资料**：算法模式、复杂度分析、题目分类等

#### Skill包含的参考文档

- [`algorithm-patterns.md`](leetcode-analyze-skill/references/algorithm-patterns.md) - 10个核心算法模式
- [`analogy-examples.md`](leetcode-analyze-skill/references/analogy-examples.md) - 形象化类比示例库
- [`code-filling-guide.md`](leetcode-analyze-skill/references/code-filling-guide.md) - 代码填空学习法
- [`complexity-guide.md`](leetcode-analyze-skill/references/complexity-guide.md) - 复杂度分析指南
- [`problem-categories.md`](leetcode-analyze-skill/references/problem-categories.md) - 题目分类和相似题目库

## 🚀 使用方法

### 方法1：直接阅读分析文档

1. 在 [`questions/`](questions/) 目录查看题目原文
2. 在 [`analysis/`](analysis/) 目录阅读对应的详细分析
3. 尝试填空练习，然后对照完整代码

### 方法2：使用AI Skill生成分析

如果你使用支持Skill的AI助手（如Claude Code、Gemini CLI、Codex等）：

1. 将新题目文件放入 `questions/` 目录
2. 告诉AI："请使用leetcode-analyze-skill分析这道题目"
3. AI会自动生成完整的分析文档到 `analysis/` 目录

#### 使用Gemini CLI

```bash
# 确保已安装Gemini CLI
# 将GEMINI.md复制到Gemini配置目录
cp leetcode-analyze-skill/GEMINI.md ~/.gemini/

# 然后在Gemini CLI中请求分析
gemini "请使用leetcode-analyze-skill分析 questions/1. 两数之和.md"
```

## 🤝 贡献指南

欢迎贡献新的题目分析！请遵循以下步骤：

1. Fork本仓库
2. 在 `questions/` 目录添加题目原文
3. 使用Skill生成分析文档或手动编写
4. 确保分析文档包含所有必需章节
5. 提交Pull Request

### 分析文档要求

- 使用 [`leetcode-analyze-skill/assets/analysis-template.md`](leetcode-analyze-skill/assets/analysis-template.md) 作为模板
- 包含形象化类比讲解
- 提供代码填空练习
- Python和C++双语言实现
- 推荐相似题目

## 📖 学习资源

### 核心算法模式（10个）

1. 双指针技巧
2. 滑动窗口
3. 动态规划
4. 回溯算法
5. 二分查找
6. DFS/BFS遍历
7. 贪心算法
8. 哈希表优化
9. 单调栈
10. 前缀和

详细说明请查看 [`algorithm-patterns.md`](leetcode-analyze-skill/references/algorithm-patterns.md)

## 🛠️ 技术栈

- **语言**：Python 3.10+, C++ 11+
- **文档格式**：Markdown
- **图表工具**：Mermaid
- **AI辅助**：Claude, Gemini, Codex...

## 📝 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

## 🌟 Star History

如果这个项目对你有帮助，请给个Star⭐️支持一下！

## 📧 联系方式

如有问题或建议，欢迎提Issue或Pull Request。

---

**Happy Coding! 💻✨**

> 记住：算法学习不是死记硬背，而是理解思维过程。通过形象化类比和互动式练习，让算法变得简单易懂！
