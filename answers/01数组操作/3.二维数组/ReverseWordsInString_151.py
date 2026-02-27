from typing import List

# 法1：使用Python内置函数法
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        words.reverse()

        result = ' '.join(words)

        return result
    
# 法2：双指针遍历法
class Solution:
    def reverseWords(self, s: str) -> str:
        words = []

        n = len(s)

        right = n - 1

        while right >= 0:
            while right >= 0 and s[right] == ' ':
                right -= 1

            if right < 0:
                break

            word_end = right

            while right >= 0 and s[right] != ' ':
                right -= 1

            word = s[right + 1:word_end + 1]

            words.append(word)

        return ' '.join(words)

# 法3：两次反转法
class Solution:
    def reverse(self, chars: List[str], left: int, right: int) -> List[str]:
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return chars

    def reverseWords(self, s: str) -> str:
        s_ = ' '.join(s.split())
        chars = list(s_)
        n = len(chars)

        self.reverse(chars, 0, n - 1)

        start = 0
        for i in range(n + 1):
            if i == n or chars[i] == ' ':
                self.reverse(chars, start, i - 1)
                start = i + 1
        return ''.join(chars) # 注意是''而不是' '
