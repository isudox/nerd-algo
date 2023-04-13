package com.leetcode;

import com.common.TreeNode;

/**
 * 129. Sum Root to Leaf Numbers
 * https://leetcode.com/problems/sum-root-to-leaf-numbers/
 */
public class Problem129 {
    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int prev) {
        if (null == node)
            return 0;
        int cur = prev * 10 + node.val;
        if (null == node.left && null == node.right)
            return cur;
        return dfs(node.left, cur) + dfs(node.right, cur);
    }
}
