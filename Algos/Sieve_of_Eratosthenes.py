class Solution:
    def sieve(self, n):
        primes = [True]*(n+1)
        primes[0] = primes[1] = False
        res = []
        for i in range(2,int(sqrt(n))+1):
            if(primes[i]):
                res.append(i)
                t = i + i
                while(t < n+1):
                    primes[t] = False
                    t+= i
        return res

# Time complexity: O(n log log n)
# Space complexity: O(n)