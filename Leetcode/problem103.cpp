// Leetcode Problem 103: Binary Zig-Zag Level order traversal
// Difficulty: Medium
// https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> answer = {};
        if(root == nullptr)
            return answer;
        vector<vector<TreeNode*>> queue = {{root}};
        int flag = 0;
        int ele = 1;   // # nodes in the current list   
        int queue_index = 0;   // current queue index
        int counter = 0;    // even : left to right, odd : right to left
        do{
            flag = 0;
            vector<int> elements = {};
            vector<TreeNode*> nodes = {};
            int i = ele;
            // cout << "Value of i  " << i << endl;
            int new_elements = 0;   // new nodes in the next level
            while(i > 0){
                TreeNode* current_node = queue[queue_index][i-1];
                // cout << "Current Node : " << current_node -> val << endl;
                elements.push_back(current_node->val);
                if(counter % 2 == 0){
                    if(current_node->left != nullptr){
                        nodes.push_back(current_node->left);
                        flag = 1;
                        new_elements++;
                    }
                    if(current_node->right != nullptr){
                        nodes.push_back(current_node->right);
                        flag = 1;
                        new_elements++;
                    }
                }
                else{
                    if(current_node->right != nullptr){
                        nodes.push_back(current_node->right);
                        flag = 1;
                        new_elements++;
                    }
                    if(current_node->left != nullptr){
                        nodes.push_back(current_node->left);
                        flag = 1;
                        new_elements++;
                    }
                }
                i--;
                // cout << "value of i : " << i << endl;
            }
            counter++;
            // cout << "NODES : " << endl;
            // for(TreeNode* i : nodes)
            //     cout << i->val << endl;
            // cout << "new elements : " << new_elements << endl;
            if(flag){
                ele = new_elements;
                queue_index++;
                queue.push_back(nodes);
            }
            answer.push_back(elements);
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
// 2. We maintain a counter to track the current level's order (left to right or right to left).
// 3. For each level, we create a list of node values and a list of child nodes for the next level.
// 4. Depending on the counter's parity, we add child nodes in the appropriate order.
// 5. We add the list of node values to the answer and update the queue with the child nodes.
// 6. We continue this process until all levels have been processed.