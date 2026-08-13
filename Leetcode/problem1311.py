# Leetcode Problem 1311 : Get Watched Videos by Your Friends
# Difficulty : Medium
# URL : https://leetcode.com/problems/get-watched-videos-by-your-friends/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        length = len(watchedVideos)
        counter = {}
        queue = deque()
        visited = {i : False for i in range(length)}
        def bfs(start_node):
            queue.append([start_node])
            visited[start_node] = True
            curr_level = 0
            while(queue):
                nodes = queue.popleft()
                new_friends = []
                for node in nodes:
                    for friend in friends[node]:
                        if(not visited[friend]):
                            visited[friend] = True
                            new_friends.append(friend)
                    if(curr_level == level):
                        for video in watchedVideos[node]:
                            if(video in counter):
                                counter[video] += 1
                            else:
                                counter[video] = 1
                queue.append(list(set(new_friends)))
                if(curr_level == level):
                    break
                curr_level +=1
        bfs(id)
        sorted_dict = sorted(counter.items(), key= lambda x: (x[1], x[0]))
        result = []
        for val in sorted_dict:
            result.append(val[0])
        return result

# Time complexity : O(n log n) where n is the number of videos watched by friends at the given level
# Space complexity : O(n) where n is the number of videos watched by friends at the given level
# Explaination : The algorithm uses a breadth-first search (BFS) approach to explore the friends at the given level and counts the frequency of videos watched by those friends. 
# It then sorts the videos based on frequency and lexicographical order to return the final list of videos.  