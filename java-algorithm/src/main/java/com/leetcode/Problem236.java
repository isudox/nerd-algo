package com.leetcode;

import com.common.TreeNode;

import java.util.*;

/**
 * 236. Lowest Common Ancestor of a Binary Tree
 * https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 */
public class Problem236 {
    private Map<TreeNode, List<TreeNode>> paths;

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        this.paths = new HashMap<>();
        backtrack(root, p, new ArrayList<>());
        backtrack(root, q, new ArrayList<>());
        List<TreeNode> pathP = paths.get(p), pathQ = paths.get(q);
        Set<Integer> set = new HashSet<>();
        for (TreeNode node : pathP) {
            set.add(node.val);
        }
        for (int i = pathQ.size() - 1; i >= 0; i--) {
            if (set.contains(pathQ.get(i).val)) {
                return pathQ.get(i);
            }
        }
        return null;
    }

    private boolean backtrack(TreeNode cur, TreeNode target, List<TreeNode> path) {
        path.add(cur);
        if (cur == target) {
            paths.put(target, new ArrayList<>(path));
            return true;
        }
        if (cur.left != null) {
            if (backtrack(cur.left, target, path)) return true;
        }
        if (cur.right != null) {
            if (backtrack(cur.right, target, path)) return true;
        }
        path.remove(path.size() - 1);
        return false;
    }
}
