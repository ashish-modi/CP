# Leetcode Poblem 3677: Count Binary Palindromes
# Difficulty : Hard
# Link : https://leetcode.com/problems/count-binary-palindromes/
# Based on Binary Search and Math

class Solution:
    def countBinaryPalindromes(self, n: int) -> int:
        len_binary = len(bin(n)[2:])
        count = 0

        def make_palindrome(number, length):
            binary = bin(number)[2:]
            if(length % 2):
                palindrome = binary + binary[-2::-1]
            else:
                palindrome = binary + binary[::-1]
            palindrome_number = int(palindrome, 2)
            return palindrome_number

        for i in range(1,len_binary+1):
            half = (i+1)//2
            smallest = 2**(half-1)
            largest = 2**half -1
            left = smallest
            right = largest
            best = -1
            while(left <= right):
                mid = (left + right) //2
                if(make_palindrome(mid,i) > n):
                    right = mid -1
                else:
                    best = mid
                    left = mid + 1
            if(best != -1):
                count += best - smallest + 1
        return count +1

# Time Complexity : O(log^2 N) where N is the input number.
# Space Complexity : O(1) as we are using only constant space.