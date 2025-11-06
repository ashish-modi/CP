# Leetcode Problem 49: Group Anagrams
# Difficulty: Medium
# URL: https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        length = len(strs)
        anagrams = {}
        for word in strs:
            my_dct = {}
            for char in word:
                my_dct[char] = my_dct.get(char,0) +1
            
            itms = tuple(sorted(list(my_dct.items())))
            
            if(anagrams.get(itms,[])):
                anagrams[itms].append(word)
            else:
                anagrams[itms] = [word]
            
        return list(anagrams.values())
        
# Time complexity: O(N*K log K) where N is the number of strings in the input list and K is the maximum length of a string.
# Space complexity: O(N*K) for storing the grouped anagrams in the dictionary.
# Explanation: The solution groups anagrams by creating a frequency dictionary for each word, which counts the occurrences of each character.
# This frequency dictionary is then converted into a sorted tuple of items to serve as a unique key for each group of anagrams.
# The words are stored in a dictionary where the keys are these tuples, and the values are lists of words that match the character frequency.