package com.leetcode;

import com.common.TreeNode;

/**
 * 105. Construct Binary Tree from Preorder and Inorder Traversal
 * https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
 * preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
 */
public class Problem105 {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return gen(preorder, 0, preorder.length, inorder, 0, inorder.length);
    }

    private TreeNode gen(int[] preorder, int x1, int y1, int[] inorder, int x2, int y2) {
        if (x1 == y1) return null;
        TreeNode root = new TreeNode(preorder[x1]);
        int z = x2;
        while (inorder[z] != preorder[x1]) z++;
        root.left = gen(preorder, x1 + 1, z - x2 + x1 + 1, inorder, x2, z);
        root.right = gen(preorder, z - x2 + x1 + 1, y1, inorder, z + 1, y2);
        return root;
    }
}
