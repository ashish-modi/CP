# Leetcode Problem 763: Partition Labels
# Difficulty : Medium
# Link : https://leetcode.com/problems/partition-labels/
# Based on HashMap and Two Pointers

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        length = len(s)
        dictionary = {element:0 for element in s}
        for i in range(length):
            dictionary[s[i]] = i
        res = []
        def makeWord(start):
            end = start
            idx = start
            while(idx < length):
                val = dictionary[s[idx]]
                if(val > end):
                    end = val
                if(idx == end):
                    return (idx - start + 1, idx + 1)
                idx += 1
            return (length - start), length
        i = 0
        while(i < length):
            l, i = makeWord(i)
            res.append(l)
        return res
    
# Time Complexity : O(N) where N is the number of characters in the input string.
# Space Complexity : O(1) as we are using constant space for the dictionary since there are only 26 lowercase English letters.
# Explanation:
# 1. We create a dictionary to store the last occurrence index of each character in the string.
# 2. We define a helper function `makeWord` that takes a starting index and finds the end index of the partition.
# 3. We iterate through the string using two pointers to determine the partitions based on the last occurrence of characters.
# 4. We append the lengths of the partitions to the result list and return it.