package com.leetcode;

import com.common.TreeNode;

/**
 * 450. Delete Node in a BST
 * https://leetcode.com/problems/delete-node-in-a-bst/
 */
public class Problem450 {
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) {
            return null;
        }
        if (root.val > key) {
            root.left = deleteNode(root.left, key);
            return root;
        }
        if (root.val < key) {
            root.right = deleteNode(root.right, key);
            return root;
        }

        if (root.left == null && root.right == null) {
            return null;
        }
        if (root.right == null) {
            return root.left;
        }
        if (root.left == null) {
            return root.right;
        }
        TreeNode successor = root.right;
        while (successor.left != null) {
            successor = successor.left;
        }
        root.right = deleteNode(root.right, successor.val);
        successor.right = root.right;
        successor.left = root.left;
        return successor;
    }
}
