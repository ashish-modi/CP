# Problem : Split array by prime indices (medium)

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