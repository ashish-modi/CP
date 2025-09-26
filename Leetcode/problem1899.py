# Leetcode Problem 1899: Merge Triplets to Form Target Triplet
# Difficulty : Medium
# Link : https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
# Based on simple iteration and condition checking

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        length = len(triplets)
        flag1 = flag2 = flag3 = False
        for triplet in triplets:
            if(triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]):
                flag1 = True
                if(triplet[1] == target[1]):
                    flag2 = True
                if(triplet[2] == target[2]):
                    flag3 = True
            elif(triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]):
                flag2 = True
                if(triplet[0] == target[0]):
                    flag1 = True
                if(triplet[2] == target[2]):
                    flag3 = True
            elif(triplet[2] == target[2] and triplet[1] <= target[1] and triplet[0] <= target[0]):
                flag3 = True
                if(triplet[1] == target[1]):
                    flag2 = True
                if(triplet[0] == target[0]):
                    flag1 = True
        return True if flag1 and flag2 and flag3 else False

# Time Complexity : O(N) where N is the number of triplets in the input array.
# Space Complexity : O(1) as we are using constant space.