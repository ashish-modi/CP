// Problem : Binary Tree Level Order Traversal (Medium)


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