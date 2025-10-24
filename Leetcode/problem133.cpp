// LeetCode Problem 133: Clone Graph
// Difficulty: Medium
// URL: https://leetcode.com/problems/clone-graph/

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:

    Node* getClone(Node* node, vector<int> &visited, vector<Node*> &node_pointers){
        Node* new_node = new Node(node->val);
        node_pointers[node->val] = new_node;
        vector<Node*> neigh = vector<Node*>();
        visited[new_node->val] = 1;
        for(auto it:node->neighbors){
            if(!visited[it->val]){
                Node* nd = getClone(it,visited, node_pointers);
                neigh.push_back(nd);
            }
            else
                neigh.push_back(node_pointers[it->val]);
        }
        new_node->neighbors = neigh;
        return new_node;
    }

    Node* cloneGraph(Node* node) {
        
        vector<int> visited = vector<int>(103,0);
        vector<Node*> node_pointers = vector<Node*>(103);
        if(!node) return node;
        Node* new_node = getClone(node, visited, node_pointers);
        return new_node;
    }
};

// Time Complexity: O(N + E) where N is the number of nodes and E is the number of edges in the graph.
// Space Complexity: O(N) for the recursion stack and the additional data structures used.  
// Explanation: The function uses DFS to traverse the graph and clone each node and its neighbors recursively.  