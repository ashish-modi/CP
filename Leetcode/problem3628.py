# Leetcode Problem 3628: Maximum number of Subsequences after one inserting
# Difficulty: Medium 
# https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/description/

class Solution:
    def numOfSubsequences(self, s: str) -> int:
        length = len(s)
        preL = [0]* length
        preLC = [0]*length
        sufT = [0]*length
        sufCT = [0]*length
        l_count = lc_count = 0

        for i in range(length):
            if(s[i] == "L"):
                l_count +=1
            elif(s[i] == "C"):
                if(l_count > 0):
                    lc_count += l_count
            preL[i] = l_count
            preLC[i] = lc_count
        ct_count = t_count = 0
        for i in range(-1, -length -1 , -1):
            if(s[i] == "C"):
                if(t_count > 0):
                    ct_count += t_count
            elif(s[i] == "T"):
                t_count +=1
            sufT[i] = t_count
            sufCT[i] = ct_count
        # print("pre L : ", preL)
        # print("pre LC : ", preLC)
        # print("Suf T : ", sufT)
        # print("Suf CT : ", sufCT)
        base = [0]* length
        gain = [0]*length
        total = 0
        for i in range(length):
            if(s[i] == "C"):
                total += preL[i] * sufT[i]
        # print("TOTAL : ", total)
        max_total = total
        for i in range(length):
            gain = max(sufCT[i], preL[i]*sufT[i], preLC[i])
            if(total + gain > max_total):
                max_total = total + gain
        # print("Max total : ", max_total)
        return max_total
        