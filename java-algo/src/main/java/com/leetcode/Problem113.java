package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * 113. Path Sum II
 * https://leetcode.com/problems/path-sum-ii/
 */
public class Problem113 {
    private List<List<Integer>> ans = new ArrayList<>();

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if (root == null) return ans;
        dfs(root, new ArrayList<>(), targetSum);
        return ans;
    }

    private void dfs(TreeNode node, List<Integer> path, int target) {
        path.add(node.val);
        target -= node.val;
        if (node.left == null && node.right == null) {
            if (target == 0) ans.add(new ArrayList<>(path));
        }
        if (node.left != null) dfs(node.left, path, target);
        if (node.right != null) dfs(node.right, path, target);
        path.remove(path.size() - 1);
    }
}
