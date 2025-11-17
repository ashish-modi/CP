// Leetcode Problem 102 : Binary Tree Level Order Traversal 
// Difficulty: Medium
// https://leetcode.com/problems/binary-tree-level-order-traversal/


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {

    vector<vector<int>> answer = {};        // to store all the elements in level order traversal
	if(root == nullptr)
		return(answer);
    vector<vector<TreeNode*>> queue = {{root}};    // to store the nodes in level order traversal
    int queue_index = 0;    // current index of the queue
    int ele = 1;    // number of elements in the list
    int flag = 0;    // denotes whether a new node has been added to the queue
    do{
        vector<int> elements = {};
        vector<TreeNode*> nodes = {};
        int new_elements = 0;
        flag = 0;
        int i = 0;      // to iterate over the elements of queue
        while(i < ele){
            TreeNode* parent = queue[queue_index][i];
            elements.push_back(parent->val);
            if(parent->left != nullptr){
                nodes.push_back(parent->left);
                new_elements++;
                flag = 1;
            }
            if(parent->right != nullptr){
                nodes.push_back(parent->right);
                new_elements++;
                flag = 1;
            }
            i++;
        }
        if(flag){
            queue.push_back(nodes);
            queue_index++;
        }
        answer.push_back(elements);
        // cout << "nodes : " << endl;
        // for(TreeNode* value: nodes)
        //     cout << value->val << endl;
        // cout << "elements" << endl;
        // for(int val: elements)
        //     cout << val << endl;
        ele = new_elements;   
        if(flag == 0)
            break;
    }while(flag);
    return answer;
    }
};

// Time Complexity : O(N) where N is the number of nodes in the binary tree.
// Space Complexity : O(W) where W is the maximum width of the binary tree (due to the queue).
// Explanation:
// 1. We use a queue to perform level order traversal of the binary tree.
// 2. We start with the root node in the queue and iterate until there are no more nodes to process.
// 3. For each level, we create a list of node values and a list of child nodes for the next level.
// 4. We add the list of node values to the answer and update the queue with the child nodes.
// 5. We continue this process until all levels have been processed.