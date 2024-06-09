#include <iostream>
#include <queue>

using std::cout;
using std::endl;
using std::queue;

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

class TreeNode {
    public:
        int val;
        TreeNode* left = nullptr;
        TreeNode* right = nullptr;

        TreeNode (int val) {
            val = val;
        }
};


// Insert a new node and return the root of the tree
TreeNode* insert(TreeNode* root, int val) {
    if (!root) {
        return new TreeNode(val);
    }

    if (val > root->val) {
        root->right = insert(root->right, val);
    }
    else if (val < root->val) {
        root->left = insert(root->left, val);
    }
    return root;
}


// Return the minimum value node of the root
TreeNode* minValueNode(TreeNode* root) {
    TreeNode* curr = root;
    while (curr && curr->left) {
        curr = curr->left;
    }
    return curr;
}


// Remove a node and return the root of the tree
TreeNode* remove(TreeNode* root, int val) {
    if (!root) {
        return nullptr;
    }

    if (val > root->val) {
        root->right = remove(root->right, val);
    }
    else if (val < root->val) {
        root->left = remove(root->left, val);
    }
    else {
        if (!root->left) 
            return root->right;
        else if (!root->right)
            return root->left;
        else {
            TreeNode* minNode = minValueNode(root->right);
            root->val = minNode->val;
            root->right = remove(root->right, minNode->val);
        }
    }
    return root;
}