from typing import List
import sys

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])

        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
    
        for i in range(m):
            for j in range(n):
                self.prefix[i + 1][j + 1] = (self.prefix[i][j + 1]
                                             + self.prefix[i + 1][j]
                                             - self.prefix[i][j]
                                             + matrix[i][j])
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = (self.prefix[row2 + 1][col2 + 1]
                - self.prefix[row2 + 1][col1]
                - self.prefix[row1][col2 + 1]
                + self.prefix[row1][col1])
        return result
"""
假定评测系统会以如下的文本格式发送数据：
3 4 (代表矩阵有 3 行 4 列)
1 2 3 4 (矩阵第 0 行)
5 6 7 8 (矩阵第 1 行)
9 10 11 12 (矩阵第 2 行)
2 (代表接下来有 2 次区域查询)
0 0 1 1 (第 1 次查询：左上角 0,0，右下角 1,1)
1 2 2 3 (第 2 次查询：左上角 1,2，右下角 2,3)
"""
if __name__ == "__main__":
    line_1 = sys.stdin.realine().strip()
    if not line_1:
        exit()

    m , n = map(int, line_1.split())

    matrix = []
    for _ in range(m):
        row = list(map(int, sys.stdin.readline().split()))
        matrix.append(row)

    num_matrix = NumMatrix(matrix)

    q_line = sys.stdin.readline().strip()
    if q_line:
        q = int(q_line)

        for _ in range(q):
            row1, col1, row2, col2 = map(int, sys.stdin.readline().split())

            result = num_matrix.sumRegion(row1, col1, row2, col2)
            print(result)
