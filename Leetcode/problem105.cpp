// Problem : Construct binary tree from preorder and inorder traversal (Medium)

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
    pair<TreeNode*, int> tree(vector<int>& preorder,  vector<int>& inorder, map<int,int>& dict, int start, int end, int root_index){
        if(start > end)
            return {nullptr, root_index};
        TreeNode * node = new TreeNode(preorder[root_index]);
        int index = dict.at(node->val);

        auto l = tree(preorder, inorder, dict, start, index -1, root_index +1);
        node->left = l.first;
        
        auto r = tree(preorder, inorder, dict, index + 1, end, l.second);
        node->right = r.first;
        return {node, r.second};
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int length = inorder.size();
        map<int,int> dict = {};
        for(int i = 0; i< length ; i++)
            dict[inorder[i]] = i;
        pair<TreeNode*, int> p = tree(preorder, inorder, dict, 0, length-1, 0);
        return p.first;
    }
};