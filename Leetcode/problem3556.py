# Leetcode problem 3556: Sum of Largest Primes substrings
# Difficulty: Medium
# https://leetcode.com/problems/sum-of-largest-primes-substrings/

class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        length = len(s)
        dictionary = {}
        primes = []
        def is_prime(number):
            if(number == 2 or number == 3):
                return True
            if(number < 2):
                return False
            for i in range(2, int(sqrt(number))+1):
                if(number %i == 0):
                    return False
            return True
            
        for i in range(length):
            for j in range(i+1,length+1):
                number = int(s[i:j])
                if not (dictionary.get(number,0)):
                    if is_prime(number):
                        dictionary[number] = 1
                        primes.append(number)
                    else:
                        dictionary[number] = 0
        sorted_primes = sorted(primes, reverse= True)
        total = 0
        for i in range(min(len(primes),3)):
            total += sorted_primes[i]
        return total

# Time complexity: O(n^3) where n is the length of the string s
# Space complexity: O(m) where m is the number of distinct substrings of s  
# Explanation:
# The function calculates the sum of the three largest prime numbers that can be formed
# from substrings of the input string s. It generates all possible substrings, checks if
# they are prime using the is_prime helper function, and stores them in a dictionary to
# avoid duplicates. Finally, it sorts the list of prime numbers and sums the top three.