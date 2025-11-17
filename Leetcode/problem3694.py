# Leetcode problem 3694:  Distinct Points reachable After substring Removal
# Difficulty : Medium
# Link : https://leetcode.com/problems/distinct-points-reachable-after-substring-removal
# Based on Prefix Sum and Hashing

class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        length = len(s)
        result = set()
        count= [0]*length
        count_u = count_d = count_l = count_r = 0
        for i in range(length):
            if(s[i] == "U"):
                count_u +=1
            elif(s[i]== "D"):
                count_d +=1
            elif(s[i]== "L"):
                count_l +=1
            else:
                count_r +=1
            count[i] = [count_u, count_d, count_l, count_r]
        total = count[-1]
        for i in range(length - k + 1):
            end = i + k - 1
            end_dp = count[end]
            start_dp = count[i - 1] if i > 0 else [0, 0, 0, 0]
    
            c_u = total[0] - (end_dp[0] - start_dp[0])
            c_d = total[1] - (end_dp[1] - start_dp[1])
            c_l = total[2] - (end_dp[2] - start_dp[2])
            c_r = total[3] - (end_dp[3] - start_dp[3])
    
            x = c_r - c_l
            y = c_u - c_d
            result.add((x, y))
        return len(result)
    
# Time Complexity : O(N) where N is the number of characters in the input string.
# Space Complexity : O(N) in the worst case, where all points are distinct.
# Explaination :
# The function distinctPoints takes a string s and an integer k as input and returns the number of distinct points reachable after removing a substring of length k from s.
# It uses prefix sums to keep track of the counts of each direction (U, D, L, R) at each position in the string.
# Then, for each possible substring of length k, it calculates the resulting position after removing that substring and adds it to a set to ensure uniqueness.
# Finally, it returns the size of the set, which represents the number of distinct points reachable.