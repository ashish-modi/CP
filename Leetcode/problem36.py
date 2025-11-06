# Leetcode Problem 36: Valid Sudoku
# Difficulty: Medium
# URL: https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            arr_row = [0]*10
            arr_col = [0]*10
            for j in range(cols):
                if(board[i][j] != "."):
                    val = int(board[i][j])
                    arr_row[val] +=1
                    if(arr_row[val] > 1):
                        return False
                if(board[j][i] != "."):
                    v = int(board[j][i])
                    arr_col[v]+=1
                    if(arr_col[v] > 1):
                        return False
        for i in range(0,rows,3):
            for j in range(0,cols,3):
                arr = [0]*10
                for k in range(3):
                    for l in range(3):
                        if(board[i+k][j+l] != "."):
                            val = int(board[i+k][j+l])
                            arr[val] +=1
                            if(arr[val] > 1):
                                return False
        return True

# Time complexity: O(1) since the board size is fixed (9x9).
# Space complexity: O(1) since the auxiliary space used does not scale with input size
# Explanation: The solution checks the validity of a Sudoku board by verifying that each row, column, and 3x3 sub-box contains no duplicate numbers.
# It iterates through each row and column, using arrays to count occurrences of numbers from 1 to 9.
# It then checks each of the nine 3x3 sub-boxes in a similar manner.
# If any number appears more than once in any row, column, or sub-box, the function returns False; otherwise, it returns True.  