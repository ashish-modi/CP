# Leetcode Problem 784 : Letter Case Permutation
# Difficulty : Medium
# URL : https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        length = len(s)
        result =[]
        integers = ["0", "1", "2", "3", "4", "5", '6', '7', '8','9']
        def helper(index, string):
            if(index == length):
                result.append(string)
                return
            
            if(s[index] not in integers):
                helper(index+1, string+ s[index].lower())
                helper(index+1, string+ s[index].upper())
            else:
                helper(index+1, string+s[index])
        helper(0, "")
        return result

# Time Complexity: O(2^N * N), where N is the number of letters in the string
# Space Complexity: O(2^N * N)
# Explaination : The algorithm explores all possible combinations of letter cases for each character in the string, 
# leading to 2^N possibilities, and for each possibility, it takes O(N) time to construct the resulting string.