# Leetcode problem 752 : Open the lock
# Difficulty : Medium
# URL : https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        states = {}
        queue = deque([(target,0)])
        visited = {target:1}

        end = {}
        for i in range(len(deadends)):
            end[deadends[i]] = 1
        while(queue):
            queue_ele = queue.popleft()
            element, level = queue_ele[0], queue_ele[1]
            if(element == '0000'):
                return level
            neighbors = []
            for i in range(4):
                nxt = ""
                prv = ""
                for j in range(4):
                    if(i == j):
                        nxt += str(int(element[i]) + 1) if element[i] != '9' else '0'
                        prv += str(int(element[i]) - 1) if element[i] != '0' else '9'
                    else:
                        nxt += element[j]
                        prv += element[j]
                if(not end.get(nxt,0)):
                    neighbors.append(nxt)
                if(not end.get(prv,0)):
                    neighbors.append(prv)
                
            # print("Neighbors : ", neighbors)
            for neigh in neighbors:
                if neigh == '0000':
                    return level + 1
                if(not visited.get(neigh,0)):
                    visited[neigh] = 1
                    queue.append((neigh, level + 1))
        else:
            return -1
        
# Time complexity : O(N) where N is the number of possible states of the lock
# Space complexity : O(N) where N is the number of possible states of the lock
# Explanation : We can use a breadth first search to find the minimum number of moves required to reach the target state from the initial state.
# We can generate all the possible states from the current state by changing each wheel one step forward or backward. 
# We can use a queue to keep track of the states to be explored and a set to keep track of the visited states. 
# We also need to check if the generated state is a deadend or not before adding it to the queue.       