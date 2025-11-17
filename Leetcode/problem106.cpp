// Leetcode Problem 106 : construct binary tree from inorder and postorder traversal
// Difficulty: Medium
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


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
    pair<TreeNode*, int> tree(vector<int>& inorder_remaining, vector<int>& postorder, TreeNode* root, int index){
        map<int, int> dictionary;
        if(inorder_remaining.empty() || index < 0){
            // cout << "inorder empty " << endl;
            return {nullptr, index+1};
        }
        // cout << " Inorder elements : " << endl;
        for(int i = 0; i < inorder_remaining.size(); i++){
            dictionary[inorder_remaining[i]] = i;
            // cout << inorder_remaining[i] << endl;
        }

        // cout << " INDEX : " << index << endl;
        root->val = postorder[index];
        int inorder_index = dictionary[root->val];
        
        // cout << "INDEX FOR NEW ROOT : " << inorder_index <<  " ROOT : " <<  root-> val << endl;
        vector<int> left(inorder_remaining.begin(), inorder_remaining.begin() + inorder_index);
        vector<int> right(inorder_remaining.begin() + inorder_index+1, inorder_remaining.end());
    
        pair<TreeNode*,int> right_tree = tree(right, postorder, new TreeNode(), index-1); // right side
        // return remaining after assigning the right tree then pass the tree to the left
        
        pair<TreeNode*, int> left_tree= tree(left, postorder, new TreeNode(), right_tree.second - 1); // left side
        root->left = left_tree.first;
        root->right = right_tree.first;
        return {root, left_tree.second};
    }
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int length = postorder.size();
        TreeNode* null_tree = new TreeNode();
        pair<TreeNode*, int> res = tree(inorder, postorder, null_tree,length-1);
        return res.first;
    }
};

// Time Complexity : O(N) where N is the number of nodes in the binary tree.
// Space Complexity : O(H) where H is the height of the binary tree (due to recursive stack) and O(N) for the hashmap.
// Explanation:
// 1. We create a hashmap to store the indices of the inorder traversal for quick access.
// 2. We define a recursive function that takes the current inorder elements, postorder traversal, the current root node, and the current index in the postorder traversal.
// 3. The base case checks if the inorder elements are empty or if the index is less than 0; if so, we return nullptr.
// 4. We set the value of the current root node to the value at the current index in the postorder traversal.
// 5. We find the index of this value in the inorder traversal using the hashmap.
// 6. We split the inorder elements into left and right subtrees.
// 7. We recursively build the right and left subtrees using the appropriate inorder elements and updated indices from the postorder traversal.
// 8. Finally, we return the constructed tree's root node.