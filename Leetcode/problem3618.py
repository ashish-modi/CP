# Leetcode Problem 3618 : Split array by prime indices (medium)
# Difficulty : Medium
# Link : https://leetcode.com/problems/split-array-by-prime-indices/

class Solution:
    def isPrime(self,integer):
        if(integer < 2):
            return False
        if(integer == 2):
            return True
        for i in range(2,int(sqrt(integer))+1):
            if(integer%i == 0):
                return False
        return True
        
    def splitArray(self, nums: List[int]) -> int:
        sumA = 0
        sumB = 0
        for i in range(len(nums)):
            prime = self.isPrime(i)
            if(prime):
                sumA += nums[i]
            else:
                sumB += nums[i]
        # print("A : ", sumA)
        # print("B: ", sumB)
        return abs(sumA - sumB)
    
# Time Complexity : O(n * sqrt(n)) where n is the length of the array
# Space Complexity : O(1)
# Explanation : We iterate through the array and for each index check if it is prime or not. 
# If it is prime we add the element to sumA else to sumB. Finally we return the absolute difference of sumA and sumB.
