package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1382. Balance a Binary Search Tree
 * https://leetcode.com/problems/balance-a-binary-search-tree/
 */
public class Problem1382 {
    public TreeNode balanceBST(TreeNode root) {
        List<Integer> vals = new ArrayList<>();
        traverse(root, vals);
        return build(vals);
    }

    private void traverse(TreeNode root, List<Integer> list) {
        if (root == null) {
            return;
        }
        traverse(root.left, list);
        list.add(root.val);
        traverse(root.right, list);
    }

    private TreeNode build(List<Integer> vals) {
        int n = vals.size();
        if (n == 0) {
            return null;
        }
        int mid = n / 2;
        TreeNode root = new TreeNode(vals.get(mid));
        root.left = build(vals.subList(0, mid));
        root.right = build(vals.subList(mid + 1, n));
        return root;
    }
}
