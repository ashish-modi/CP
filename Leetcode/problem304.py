# Leetcode Problem 304: Range Sum Query 2D - Immutable
# Difficulty: Medium
# URL: https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.dp = [[0]*(cols+1) for _ in range(rows+1)]
        for i in range(rows):
            for j in range(cols):
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2][col2] - self.dp[row1-1][col2] - self.dp[row2][col1 -1] + self.dp[row1 -1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Time Complexity: O(1) for each sumRegion query after O(M*N) preprocessing time in the constructor, where M and N are the dimensions of the matrix.
# Space Complexity: O(M*N) for storing the prefix sum matrix.
# Explanation:
# 1. We create a 2D prefix sum array `dp` where `dp[i][j]` contains the sum of all elements from the top-left corner (0,0) to (i,j).
# 2. The sumRegion function calculates the sum of the specified submatrix using the inclusion-exclusion principle on the prefix sums.