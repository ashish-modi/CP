# Leetcode problem 791 : Custom Sort String
# Difficulty : Medium
# Url : https://leetcode.com/problems/custom-sort-string/

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        length1 = len(order)
        length2 = len(s)
        count = {}
        present = {}
        visited = {}
        for i in range(length2):
            present[s[i]] = 1
            if(count.get(s[i],0)):
                count[s[i]] +=1
            else:
                count[s[i]] = 1
        res = ""
        for i in range(length1):
            if present.get(order[i],0):
                res += order[i]*count[order[i]]
                visited[order[i]] = 1
        for i in range(length2):
            if not visited.get(s[i],0):
                res += s[i]
        return res



# Time complexity : O(n + m), where n is the length of order and m is the length of s.
# Space complexity : O(n + m), where n is the length of order and m is the length of s.
# Explanation : We can use a hash map to count the frequency of each character in s and another hash map to check if a character is present in order. 
# We iterate through order and for each character, we check if it is present in s. If it is, we add it to the result string the number of times it appears in s. 
# We also mark that character as visited. After iterating through order, we iterate through s and add any character that is not visited to the result string.