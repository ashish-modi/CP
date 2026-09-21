class Solution:
    def createarray(self,string):
        length = len(string)
        array = [0]*length                              # array to keep track of the prefixes
        j = 0
        for i in range(1,length):
            if(string[i] == string[j]):          # characters match : set that the next character has to be compared 
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
        return array



    def stringmatching(self,left : int, right: int, s:str, p: str, array):
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
        
# Geeks for Geeks : https://www.geeksforgeeks.org/problems/search-pattern0205/1
class Solution:
    def search(self, pat, txt):
        # code here
        l_pattern = len(pat)
        l_txt = len(txt)
        lps = [0]*l_pattern
        def create_array():
            for i in range(1,l_pattern):
                j = lps[i-1]
                if(pat[i] == pat[j]):
                    lps[i] = j+1
                else:
                    while(j != 0):
                        j = lps[j-1]
                        if(pat[i] == pat[j]):
                            lps[i] = j+1
                            break
                    else:
                        lps[i] = j
        create_array()

# Explaination of create_array function : We create an array to keep track of the prefixes of the pattern. 
# We iterate through the pattern and compare the characters. If the characters match, we set the next character to be compared. 
# If the characters don't match, we check the previous character in the pattern and compare it with the current character. If they match, we set the next character to be compared. 
# If they don't match, we set the next character to be compared to 0.

        result = []
        j=0
        for i in range(l_txt):
            while(txt[i] != pat[j] and j > 0):
                j = lps[j-1]
            if(txt[i] == pat[j]):
                j+=1
    
            if(j == l_pattern):
                result.append(i-j+1)
                j=lps[j-1]


        return result
        
# Time Complexity : O(n) where n is the length of the string
# Space Complexity : O(m) where m is the length of the pattern
# Explanation : We create an array to keep track of the prefixes of the pattern. 
# Then we use that array to compare the pattern with the string. 
# If we find a match, we return the index of the match. If we don't find a match, we return -1.

