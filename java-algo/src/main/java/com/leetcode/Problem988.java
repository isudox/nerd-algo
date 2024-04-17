package com.leetcode;

import com.common.TreeNode;

/**
 * 988. Smallest String Starting From Leaf
 * https://leetcode.com/problems/smallest-string-starting-from-leaf/
 */
public class Problem988 {
    private String ans = "";

    public String smallestFromLeaf(TreeNode root) {
        dfs("", root);
        return ans;
    }

    private void dfs(String cur, TreeNode node) {
        cur = (char) ('a' + node.val) + cur;
        if (node.left == null && node.right == null) {
            if (ans.isEmpty() || ans.compareTo(cur) > 0) {
                ans = cur;
            }
        }
        if (node.left != null) {
            dfs(cur, node.left);
        }
        if (node.right != null) {
            dfs(cur, node.right);
        }
    }
}
