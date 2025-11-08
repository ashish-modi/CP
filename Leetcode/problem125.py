# Leetcode Problem 125: Valid Palindrome
# Difficulty: Easy
# URL: https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(s)
        
        for i in range(len(l)):
            c_ascii = ord(l[i])
            if(c_ascii >= 65 and c_ascii <=90):
                l[i] = chr(c_ascii + 32)
            elif(c_ascii >= 97 and c_ascii <= 122) or (c_ascii >=48 and c_ascii <= 57):
                pass
            else:
                l[i] = ""
        final_string = "".join(l)
        return final_string == final_string[::-1]
    
# Time complexity:
# O(N) - We traverse the string twice: once to clean it and once to check for palindrome.
# Space complexity:
# O(N) - We use additional space to store the cleaned string.
# Explanation:
# The solution first processes the input string to remove non-alphanumeric characters and convert all letters to lowercase. 
# It then checks if the cleaned string is equal to its reverse, which determines if it is a palindrome.