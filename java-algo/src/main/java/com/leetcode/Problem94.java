package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;
/**
 * 94. Binary Tree Inorder Traversal
 * https://leetcode.com/problems/binary-tree-inorder-traversal/
 */
class Problem94 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null) return ans;
        if (root.left != null) ans = inorderTraversal(root.left);
        ans.add(root.val);
        if (root.right != null) ans.addAll(inorderTraversal(root.right));
        return ans;
    }
}

