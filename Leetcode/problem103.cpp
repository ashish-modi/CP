// Problem : Binary Zig-Zag Level order traversal (Medium)

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