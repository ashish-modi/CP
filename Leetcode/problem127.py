# Leetcode Problem 127: Word Ladder
# Difficulty : Hard
# Link : https://leetcode.com/problems/word-ladder/
# Based on BFS Algorithm
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)
        length = len(wordList)
        word_length = len(beginWord)
        visited = {}
        graph = {}
        nodes = {}
        for i in range(length):
            visited[wordList[i]] = 0
            for j in range(word_length):
                node = wordList[i][:j] + "*" + wordList[i][j+1:]
                
                nodes[wordList[i]] = nodes.get(wordList[i],[]) + [node]
                graph[node] = graph.get(node,[]) + [wordList[i]]

        def bfs(node):
            q = deque()
            q.append(node)
            visited[node] = 1
            elements = 1
            new_elements = 0
            level = 1
            while q:
                n = q.popleft()
                elements -=1
                neighbours = []
                for node in nodes[n]:
                    for nghbr in graph[node]:
                        if(nghbr != n):
                            neighbours.append(nghbr)
                for neigh in neighbours:
                    if(not visited[neigh]):
                        visited[neigh] = 1
                        q.append(neigh)
                        new_elements +=1
                        if(neigh == endWord):
                            return level + 1
                if(elements == 0):
                    elements = new_elements
                    new_elements = 0
                    level +=1
            return -1
        l = bfs(beginWord)
        
        return 0 if l == -1 else l
                

# Time Complexity: O(N * M^2) where N is the number of words in the wordList and M is the length of each word.
# Space Complexity: O(N * M) for storing the graph and nodes.
# Explanation: The code constructs a graph where each word is connected to other words that differ by one letter. 
# It then uses BFS to find the shortest path from beginWord to endWord.


