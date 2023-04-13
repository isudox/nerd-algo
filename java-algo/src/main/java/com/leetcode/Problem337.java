package com.leetcode;

import com.common.TreeNode;

import java.util.HashMap;
import java.util.Map;

public class Problem337 {

    private Map<TreeNode, Integer> memo1 = new HashMap<>();
    private Map<TreeNode, Integer> memo2 = new HashMap<>();

    public int rob(TreeNode root) {
        return dfs(root, true);
    }

    private int dfs(TreeNode node, boolean can) {
        if (node == null) {
            return 0;
        }
        if (can && memo2.containsKey(node)) {
            return memo2.get(node);
        }
        if (!can && memo1.containsKey(node)) {
            return memo1.get(node);
        }
        int ret = dfs(node.left, true) + dfs(node.right, true);
        if (can) {
            ret = Math.max(ret, node.val + dfs(node.left, false) + dfs(node.right, false));
        }
        if (can) {
            memo2.put(node, ret);
        } else {
            memo1.put(node, ret);
        }
        return ret;
    }
}
