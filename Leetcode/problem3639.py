class Solution:
    def binaryS(self, order, left, right, length, k):
        mid = (left + right)//2
        r = [1]*length
        for i in range(mid+1):
            r[order[i]] = 0
        total = 0
        count = 0
        for i in range(length):
            if(r[i]):
                count += r[i]
            else:
                total += (count * (count + 1))//2
                count = r[i]
        total += (count *(count +1)) // 2
        actual = (length * (length+1))//2
        # print("Left : ", left, " Right : ", right , "Mid : ", mid ," Total : ", actual - total)
        if(left == right):
            if(actual - total >= k):
                return left
            else:
                return -1
        if(actual - total >= k):
            return self.binaryS(order, left, mid, length, k)
        else:
            return self.binaryS(order, mid + 1, right, length, k)
        


    def minTime(self, s: str, order: List[int], k: int) -> int:
        length = len(order)
        return self.binaryS(order, 0, length-1, length, k)
