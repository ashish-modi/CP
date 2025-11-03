# Leetcode Problem 1314: Matrix Block Sum
# Difficulty: Medium
# URL: https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        answer = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                answer[i][j] = 0
                left_wall = i -k
                right_wall = i+k
                up_wall = j -k
                down_wall = j+k
                for l in range(rows):
                    for m in range(cols):
                        if(l >= left_wall and l <= right_wall and m >= up_wall and m <= down_wall):
                            answer[i][j] += mat[l][m]
        return answer
    
# Time complexity: O(M*N*(2k+1)*(2k+1)) where M and N are the number of rows and columns in the matrix respectively.
# Space complexity: O(M*N) for the answer matrix.
# Explanation: The solution iterates through each cell in the matrix and calculates the sum of all elements within the k-distance block around that cell by checking all other cells in the matrix.