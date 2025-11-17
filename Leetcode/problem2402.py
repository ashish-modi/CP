# Leetcode Problem 2402: Meeting Rooms III
# Difficulty: Hard
# URL: https://leetcode.com/problems/meeting-rooms-iii/

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        length = len(meetings)
        meetings.sort()
        room_number = [i for i in range(n)]
        index = 0
        room_count = [0]*length
        heap = []
        heapq.heapify(room_number)
        start = 0
        while(index < length):
            while(heap and heap[0][0] <= meetings[index][0]):
                end_time, v_room = heapq.heappop(heap)
                heapq.heappush(room_number, v_room)
            if(room_number):
                room = heapq.heappop(room_number)
                room_count[room] +=1
                heapq.heappush(heap,(meetings[index][1]- meetings[index][0] + max(start, meetings[index][0]) ,room))
                index +=1
            else:   
                if(heap):
                    end_time, v_room = heapq.heappop(heap)
                    heapq.heappush(room_number, v_room)
                    start = end_time 

        maximum = room_count[0]
        max_index = 0
        for i in range(1,length):
            if(room_count[i] > maximum):
                maximum = room_count[i]
                max_index = i
        return max_index
    
# Time Complexity: O(M log N) where M is the number of meetings and N is the number of rooms.
# Space Complexity: O(N) for the heaps used to manage room availability.
# Explanation:
# 1. We sort the meetings based on their start times to process them in order.
# 2. We use two heaps: one to manage available rooms and another to track ongoing meetings.
# 3. For each meeting, we check if any rooms have become available by comparing the current meeting's start time with the end times in the ongoing meetings heap.
# 4. If a room is available, we assign it to the current meeting and update the room's end time.
# 5. If no rooms are available, we wait until the earliest room becomes free and then assign it to the current meeting.
# 6. We keep track of how many meetings each room has hosted and finally return the room with the maximum count.