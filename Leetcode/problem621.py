# Leetcode Problem 621: Task Scheduler
# Difficulty: Medium
# URL: https://leetcode.com/problems/task-scheduler/

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        dictionary = {}
        for i in range(length):
            dictionary[tasks[i]] = dictionary.get(tasks[i],0) + 1
        heap = []
        for key, value in dictionary.items():
            heap.append([-value, key])
        
        heapq.heapify(heap)
        queue = deque()
        count = 0
        while(heap or queue):
            count +=1
            if(heap):
                element = heapq.heappop(heap) 
                element[0] +=1
            
                if(element[0]):
                    queue.append((element, count + n))

            if queue and queue[0][1] == count:
                ele, _ = queue.popleft()
                heapq.heappush(heap, ele)
            
        return count

# Time complexity: O(T log k) where T is the total number of tasks and k is the number of unique tasks. Each task is pushed and popped from the heap.
# Space complexity: O(k) where k is the number of unique tasks stored in the heap.
# Explanation: The solution uses a max-heap to always execute the task with the highest remaining count. A queue is used to manage the cooldown period for tasks.
# Each time a task is executed, its count is decremented and if it still has remaining executions, it is added to the queue with the time it can be executed again.
