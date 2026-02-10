# 贡献指南

感谢你对LeetCoding项目的关注！我们欢迎任何形式的贡献。

## 如何贡献

### 1. 添加新题目分析

#### 方法A：使用AI Skill生成（推荐）

1. Fork本仓库
2. 在 `questions/` 目录添加题目原文（Markdown格式）
3. 使用AI助手（Claude/Gemini/Codex）配合 `leetcode-analyze-skill` 生成分析文档
4. 确保生成的分析文档包含所有必需章节
5. 提交Pull Request

**示例**：
```bash
# 1. 添加题目文件
echo "题目内容" > questions/283. 移动零.md

# 2. 使用AI生成分析（以Gemini为例）
gemini "请使用leetcode-analyze-skill 分析 questions/283. 移动零.md"

# 3. 检查生成的文件
ls analysis/283-MoveZeroes-思路分析.md

# 4. 提交
git add questions/283.\ 移动零.md analysis/283-MoveZeroes-思路分析.md
git commit -m "Add question: LeetCode 283 - 移动零"
git push origin master
```

#### 方法B：手动编写

1. Fork本仓库
2. 在 `questions/` 目录添加题目原文
3. 参考 [`leetcode-analyze-skill/assets/analysis-template.md`](leetcode-analyze-skill/assets/analysis-template.md) 手动编写分析文档
4. 将分析文档保存到 `analysis/` 目录，命名格式：`{题号}-{题目名称}-思路分析.md`
5. 提交Pull Request

### 2. 改进现有分析

如果你发现现有分析文档有以下问题，欢迎提交改进：

- 代码错误或可以优化
- 解释不够清晰
- 缺少边界情况说明
- 类比不够恰当
- 相似题目推荐不准确

**改进步骤**：
1. Fork本仓库
2. 修改对应的分析文档
3. 在commit message中说明改进内容
4. 提交Pull Request

### 3. 完善Skill参考文档

如果你想为 `leetcode-analyze-skill/references/` 目录下的参考文档添加内容：

- 添加新的算法模式示例
- 补充形象化类比
- 完善题目分类
- 改进复杂度分析说明

**注意**：
- `algorithm-patterns.md` 只保留最核心的10个算法模式
- 新增内容应该具有普遍性和实用性
- 保持文档的简洁性和可读性

### 4. 报告问题

发现Bug或有改进建议？请提Issue：

1. 点击 [Issues](../../issues) 标签
2. 点击 "New Issue"
3. 选择合适的Issue模板
4. 详细描述问题或建议

## 分析文档质量标准

提交的分析文档应该满足以下标准：

### 必需章节（10个）

- [ ] 📋 题目信息
- [ ] 📖 题目描述
- [ ] 🤔 题目分析
- [ ] 💡 解题思路（包含暴力和优化解法）
- [ ] 🎨 图解说明
- [ ] ✏️ 代码框架填空
- [ ] 💻 完整代码实现（Python + C++）
- [ ] ⚠️ 易错点提醒
- [ ] 🔗 相似题目推荐
- [ ] 📚 知识点总结

### 内容质量要求

- [ ] **形象化类比**：复杂概念前提供生活化类比
- [ ] **渐进式讲解**：从暴力到优化的完整推导过程
- [ ] **代码一致性**：填空练习与完整代码必须一致
- [ ] **代码可运行**：Python和C++代码都能直接运行
- [ ] **注释详细**：关键步骤有清晰的注释说明
- [ ] **复杂度分析**：准确的时间和空间复杂度分析
- [ ] **边界情况**：列出常见的边界条件和易错点
- [ ] **相似题目**：推荐2-3道相关题目

### 格式规范

- [ ] 使用标准Markdown格式
- [ ] 代码块标注语言类型（```python, ```cpp）
- [ ] 适当使用emoji增强可读性
- [ ] Mermaid图表语法正确
- [ ] 文件命名符合规范：`{题号}-{英文名称}-思路分析.md`

## 代码风格

### Python

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
    
    # 详细的注释
    for num in nums:
        # 说明这一步在做什么
        result.append(num)
    
    return result
```

### C++

```cpp
class Solution {
public:
    // 函数说明
    vector<int> solution(vector<int>& nums) {
        vector<int> result;
        
        // 详细的注释
        for (int num : nums) {
            // 说明这一步在做什么
            result.push_back(num);
        }
        
        return result;
    }
};
```

## Pull Request流程

1. **Fork仓库**
   ```bash
   # 在GitHub上点击Fork按钮
   ```

2. **克隆到本地**
   ```bash
   git clone https://github.com/marcus-ao/LeetCoding.git
   cd LeetCoding
   ```

3. **创建新分支**
   ```bash
   git checkout -b add-leetcode-283
   ```

4. **添加内容**
   ```bash
   # 添加题目和分析文档
   git add questions/283.\ 移动零.md
   git add analysis/283-MoveZeroes-思路分析.md
   ```

5. **提交更改**
   ```bash
   git commit -m "Add question: LeetCode 283 - 移动零

   - 添加题目原文
   - 添加详细分析文档
   - 包含形象化类比和代码填空练习"
   ```

6. **推送到GitHub**
   ```bash
   git push origin add-leetcode-283
   ```

7. **创建Pull Request**
   - 在GitHub上打开你的Fork
   - 点击 "Compare & pull request"
   - 填写PR描述
   - 提交PR

## Commit Message规范

使用清晰的commit message：

- `Add: LeetCode {题号} - {题目名称}` - 添加新题目
- `Fix: {题号} - 修复代码错误` - 修复错误
- `Improve: {题号} - 改进解释` - 改进现有内容
- `Update: Skill文档更新` - 更新Skill相关文档
- `Docs: 更新README` - 文档更新

**示例**：
```bash
git commit -m "Add question: LeetCode 283 - 移动零

- 添加题目原文和详细分析
- 提供双指针解法的形象化类比
- 包含Python和C++实现
- 推荐相似题目：26, 27"
```

## 审核流程

提交的PR会经过以下审核：

1. **自动检查**：
   - 文件命名是否符合规范
   - Markdown格式是否正确
   - 代码语法是否正确

2. **内容审核**：
   - 是否包含所有必需章节
   - 代码是否可运行
   - 解释是否清晰易懂
   - 是否有形象化类比

3. **合并**：
   - 审核通过后会被合并到主分支
   - 你的贡献会被记录在Contributors中

## 行为准则

- 尊重他人的贡献
- 保持友好和建设性的讨论
- 接受建设性的反馈
- 专注于项目的教育价值

## 问题和帮助

如果你在贡献过程中遇到问题：

1. 查看现有的Issues和PR
2. 阅读 [`leetcode-analyze-skill/SKILL.md`](leetcode-analyze-skill/SKILL.md)
3. 提Issue询问
4. 参考已有的分析文档作为示例

## 致谢

感谢所有为本项目做出贡献的开发者！你们的努力让算法学习变得更加简单有趣。

---

**再次感谢你的贡献！🎉**
