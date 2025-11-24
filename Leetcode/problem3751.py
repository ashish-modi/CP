# Leetcode problem 3751: Total Waviness of Numbers in a Range I
# Difficulty: Medium
# Link: https://leetcode.com/problems/total-waviness-of-numbers-in-a-range-i/

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total = 0
        for num in range(num1, num2+1):
            val = str(num)
            count = 0
            
            for i in range(1,len(val)-1):
                curr = int(val[i])
                prev = int(val[i-1])
                nxt = int(val[i+1])   
                if ((prev < curr > nxt) or (prev > curr < nxt)):
                    count +=1
            
            total +=count
        return total
    
# Time Complexity: O(n * m) where n is the range size and m is the number of digits in the number
# Space Complexity: O(1)
# Explanation:
# 1. We iterate through each number in the given range from num1 to num2.
# 2. For each number, we convert it to a string to easily access each digit.
# 3. We then check each digit (except the first and last) to see if it is a peak or a valley by comparing it with its adjacent digits.
# 4. If it is a peak or a valley, we increment the count for that number.
# 5. Finally, we sum up the counts for all numbers in the range and return the total waviness.