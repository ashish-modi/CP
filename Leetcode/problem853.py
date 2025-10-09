# Leetcode Problem 853: Car Fleet
# Difficulty: Medium
# URL: https://leetcode.com/problems/car-fleet/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(speed)
        result = deque()
        time = [0]*length
        tmp = [0]*length
        for i in range(length):
            tmp[i] = (position[i], speed[i])
        tmp.sort(reverse=True)
        # print("Tmp : ", tmp)
        for i in range(length):
            time[i] = (target - tmp[i][0])/tmp[i][1]
        # print("Time: ", time)
        result.append(time[0])
        for i in range(1,length):
            if(time[i] > result[-1]):
                result.append(time[i])
        # print("Result : ", result)
        return len(result)


# Time complexity: O(n log n)
# Space complexity: O(n)
# Explanation:
# 1. We first create a list of tuples containing the position and speed of each car.
# 2. We sort this list in descending order based on the position of the cars.
# 3. We then calculate the time it takes for each car to reach the target.
# 4. We use a deque to keep track of the fleets. We start with the first car and compare the time of each subsequent car.
# 5. If a car takes more time to reach the target than the last car in the deque, it forms a new fleet and we append its time to the deque.
# 6. Finally, we return the length of the deque, which represents the number of fleets.
