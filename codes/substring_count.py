# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".

# Count the number of ab and ba in the string

class Solution:
    def count_substr(self,s,char1, char2):
        length = len(s)
        flag_a = 0
        count = 0
        str_count = 0
        for i in range(length):
            if(s[i] == char1):
                if(flag_a):
                    count +=1
                else:
                    count = 1
                    flag_a = 1
            elif(s[i] == char2 and count > 0):
                count -=1
                str_count +=1
            else:
                flag_a = 0
                count = 0
        return str_count
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ab_count = self.count_substr(s, 'a', 'b')
        ba_count = self.count_substr(s, 'b', 'a')
        print("AB COUNT : ", ab_count)
        print("BA count : ", ba_count)
        