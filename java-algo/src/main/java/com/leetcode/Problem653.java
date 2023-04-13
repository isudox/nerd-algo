package com.leetcode;

import com.common.TreeNode;

import java.util.HashSet;
import java.util.Set;

/**
 * 653. Two Sum IV - Input is a BST
 * https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
 */
public class Problem653 {
    public boolean findTarget(TreeNode root, int k) {
        return recur(root, k, new HashSet<>());
    }

    private boolean recur(TreeNode node, int k, Set<Integer> seen) {
        if (node == null) return false;
        if (seen.contains(k - node.val)) return true;
        seen.add(node.val);
        return recur(node.left, k, seen) || recur(node.right, k, seen);
    }
}
