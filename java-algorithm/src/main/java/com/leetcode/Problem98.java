package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 98. Validate Binary Search Tree
 * https://leetcode.com/problems/validate-binary-search-tree/
 */
public class Problem98 {
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        Deque<TreeNode> q = new ArrayDeque<>();
        TreeNode prev = null;
        while (root != null || !q.isEmpty()) {
            while (root != null) {
                q.offerLast(root);
                root = root.left;
            }
            root = q.pollLast();
            if (prev != null && prev.val >= root.val) return false;
            prev = root;
            root = root.right;
        }
        return true;
    }

    public boolean isValidBST2(TreeNode root) {
        return check(root, null, null);
    }

    private boolean check(TreeNode node, TreeNode lo, TreeNode hi) {
        if (node == null) return true;
        if (lo != null && lo.val >= node.val) return false;
        if (hi != null && hi.val <= node.val) return false;
        return check(node.left, lo, node) && check(node.right, node, hi);
    }
}
