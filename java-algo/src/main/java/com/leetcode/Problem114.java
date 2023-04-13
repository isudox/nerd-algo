package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class Problem114 {
    public void flatten(TreeNode root) {
        if (root == null) return;
        List<TreeNode> list = new ArrayList<>();
        recur(root, list);
        for (int i = 0; i < list.size(); i++) {
            list.get(i).left = null;
            if (i == list.size() - 1) break;
            list.get(i).right = list.get(i + 1);
        }
    }

    private void recur(TreeNode node, List<TreeNode> list) {
        if (node == null) return;
        list.add(node);
        recur(node.left, list);
        recur(node.right, list);
    }
}
