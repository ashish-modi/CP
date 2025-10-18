# Leetcode Porblem 76 : Minimum Window Substring
# Difficulty: Hard
# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        length1= len(s)
        length2 = len(t)
        left = res = 0
        dict2 = {}
        dict1 = {}
        one = False

        minimum = float('inf')
        left_index = right_index = 0
        for i in range(length2):
            dict2[t[i]] = 1 + dict2.get(t[i],0)

        def check():
            flag = True
            for key, values in dict2.items():
                v = dict1.get(key, 0)
                if(v < 1 or v < values):
                    flag = False
                    break
            return flag

        for right in range(length1):
            dict1[s[right]] = 1 + dict1.get(s[right],0)
            
            while(check()):
                one = True
                dict1[s[left]] -=1
                if(right - left + 1 < minimum):
                    minimum = right - left + 1
                    left_index = left
                    right_index = right
                left +=1
        
        return s[left_index : right_index + 1] if one else ""
    
# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: We use two hashmaps to store the frequency of characters in t and the current window in s.
# We expand the right pointer to include more characters until we have a valid window that contains all characters from t. 
# Then, we try to contract the window from the left to find the minimum window. We keep track of the minimum length and its indices during this process. 
# If no valid window is found, we return an empty string.