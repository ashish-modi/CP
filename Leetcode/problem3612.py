# Problem : process strings with special operations 1

class Solution:
    def processStr(self, s: str) -> str:
        length = len(s)
        result =[]
        for i in range(length):
            if(s[i] == '*'):
                if(result):
                    result.pop()
            elif(s[i] == '#'):
                result += result
            elif(s[i] == '%'):
                result = result[::-1]
            else:
                result.append(s[i])
        return ("").join(result)