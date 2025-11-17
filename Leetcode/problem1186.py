
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        res = maximum = 0
        length = len(arr)
        flag = False
        picked = False
        for i in range(length):
            if(res + arr[i] >= res):
                picked = True
                res += arr[i]
            else:
                if(res > 0 and not flag):  # skipped one element
                    print("I : ", i, "setting flag")
                    flag = True
                else:
                    maximum = max(maximum, res)
                    res = 0
                    flag = False
            print("Res ; ", res)
        maximum = max(maximum, res)

        return maximum if picked else arr[0]