for _ in range(int(input())):
    n, c = map(int,input().split())
    a = list(map(int,input().split()))
    length = len(a)
    diff = [0]*length
    index = 0
    visited = [False]*length
    
    for i in range(length):
        min = float('inf')
        for j in range(length):  
            value = a[j]*(2**i)
            diff[j] = c- value 
            if(not visited[j] and diff[j] >= 0 and diff[j] < min):
                min = diff[j]
                index = j
        visited[index] = True 
        # print("DIFF : ", diff)
        # print("MIN : ", min)  

        if(min == float('inf')):
            print(length - i)
            break
    else:
        print(0)
        

