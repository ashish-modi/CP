# Leetcode Problem 127: Word Ladder
# Difficulty : Medium
# Link : https://leetcode.com/problems/word-ladder/
# Based on BFS Algorithm

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)
        length = len(wordList)
        word_length = len(beginWord)
        graph = {}
        visited = {}
        for i in range(length):
            graph[wordList[i]] = []
            visited[wordList[i]] = 0
        for i in range(length):
            for j in range(i+1, length):
                count = 0
                for k in range(word_length):
                    if(wordList[i][k] != wordList[j][k]):
                        count +=1
                if(count == 1):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])
        print("Dictionary : ", graph)
        
        def bfs(node):
            q = deque()
            q.append(node)
            visited[node] = 1
            elements = 1
            new_elements = 0
            level = 1
            
            while q:
                n = q.popleft()
                print("popped :", n)
                elements -=1
                for neigh in graph[n]:
                    # print("Neigh :" ,neigh, "of graph :", graph[n])
                    if(not visited[neigh]):
                        visited[neigh] = 1
                        q.append(neigh)
                        new_elements +=1
                        # print("Neigh:", neigh)
                        if(neigh == endWord):
                            return level + 1
                if(elements == 0):
                    print("new elements in the next level :", new_elements)
                    elements = new_elements
                    new_elements = 0
                    level +=1
            return -1
        l = bfs(beginWord)
        print("L :", l)
        return 0 if l == -1 else l

# Time Complexity : O(M * N^2) where M is the length of each word and N is the number of words in the word list.
# Space Complexity : O(M * N) for the graph and visited dictionary.

