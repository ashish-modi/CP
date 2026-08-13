# Leetcode Problem 721 : Accounts Merge
# Difficulty : Medium
# URL : https://leetcode.com/problems/accounts-merge/


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        length = len(accounts)
        acc_map = {}
        res = {}
        parent = {i: i for i in range(length)}

        def find_parent(node1):

            if(parent[node1] != node1):
                parent[node1] = find_parent(parent[node1])
            return parent[node1]

        for j in range(length):
            for i in range(1,len(accounts[j])):
                if(accounts[j][i] not in acc_map):
                    acc_map[accounts[j][i]] = j
                else:
                    parent1 = find_parent(j)
                    parent2 = find_parent(acc_map[accounts[j][i]])
                    if(parent1 != parent2):
                        parent[parent1] = parent2
        for i in range(length):
            parent[i] = find_parent(i)

        res = {}
        for key, value in parent.items():
            if value in res:
                for i in range(1,len(accounts[key])):
                    res[value].add(accounts[key][i])
            else:
                res[value] = set(accounts[key][1:])
        
        result = []
        for key, values in res.items():
            tmp = []
            tmp.append(accounts[key][0])
            tmp += sorted(values)
            result.append(tmp)
        return result

        
                    
# Time complexity : O(n*m*log(n*m)) where n is the number of accounts and m is the average number of emails per account
# Space complexity : O(n*m)
# Explaination : The solution uses a union-find data structure to merge accounts with common emails. 
# The time complexity is dominated by the union and find operations, which are nearly constant with path compression. 
# The space complexity is due to storing all unique emails and their associated accounts.