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
        
        
        
                    