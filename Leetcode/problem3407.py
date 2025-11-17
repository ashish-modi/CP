# Leetcode Problem 3407: Substring Matching pattern
# Difficulty: Easy
# Link : https://leetcode.com/problems/substring-matching-pattern/

class Solution:
    def createarray(self,string):
        length = len(string)
        array = [0]*length
        j = 0
        for i in range(1,length):
            if(string[i] == string[j]):
                array[i] = j+1
                j+=1
            else:
                while(True):
                    j = array[j-1]
                    if(string[i] == string[j]):
                        array[i] = j+1
                        j+=1
                        break
                    if(j == 0):
                        break
        # print("ARRAY :", array)
        return array



    def stringmatching(self,left : int, right: int, s:str, p: str, array):
        print("ARRAY : ", array)
        if(not p):
            return True, left
        else:
            length = len(p)
            j = 0
            while(left < right):
                
                if(s[left] == p[j]):
                    
                    left+=1
                    j+=1
                    if(j == length):
                        return True,left
                else:
                    
                    if(j == 0):
                        left+=1
                    else:
                        j = array[j-1]

            return False,right

        
    def hasMatch(self, s: str, p: str) -> bool:
        length1 = len(s)
        length2 = len(p)
        star_index = p.index("*")
        left_p = p[:star_index]
        right_p = p[star_index+1:]
        left_array = self.createarray(left_p)
        right_array = self.createarray(right_p)
        left, index = self.stringmatching(0, length1, s, left_p, left_array)
        right, index = self.stringmatching(index, length1, s, right_p, right_array)
        return True if(left and right) else False
        
        
        
                    
# Time Complexity: O(N + M) where N is the length of string s and M is the length of pattern p.
# Space Complexity: O(M) for the array used in KMP algorithm.
# Explanation: 
# We first create the KMP array for both the left and right parts of the pattern (before and after the '*').
# We then use the KMP string matching algorithm to find the left part in the string s.
# After finding the left part, we continue from the end index to find the right part in the string s.
# If both parts are found, we return True, otherwise we return False.