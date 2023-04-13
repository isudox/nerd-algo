package com.leetcode;

import com.common.TreeNode;

/**
 * 106. Construct Binary Tree from Inorder and Postorder Traversal
 * https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
 */
public class Problem106 {

    private int[] inorder;
    private int[] postorder;

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder == null || postorder.length == 0) {
            return null;
        }
        this.inorder = inorder;
        this.postorder = postorder;
        int n = postorder.length;
        return helper(0, n - 1, 0, n - 1);
    }

    private TreeNode helper(int i, int j, int x, int y) {
        if (i > j) {
            return null;
        }
        TreeNode root = new TreeNode(postorder[y]);
        if (x == y) {
            return root;
        }
        int k = i;
        while (inorder[k] != postorder[y]) {
            k++;
        }
        root.left = helper(i, k - 1, x, x + k - i - 1);
        root.right = helper(k + 1, j, x + k - i, y - 1);
        return root;
    }
}
