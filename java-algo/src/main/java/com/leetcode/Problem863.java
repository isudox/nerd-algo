package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 863. All Nodes Distance K in Binary Tree
 * https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
 */
public class Problem863 {
    private Map<Integer, TreeNode> parents = new HashMap<>();
    private List<Integer> ans = new ArrayList<>();

    public List<Integer> distanceK(TreeNode root, TreeNode target, int k) {
        pointToPar(root);
        find(target, null, k);
        return ans;
    }

    private void pointToPar(TreeNode node) {
        if (node.left != null) {
            parents.put(node.left.val, node);
            pointToPar(node.left);
        }
        if (node.right != null) {
            parents.put(node.right.val, node);
            pointToPar(node.right);
        }
    }

    private void find(TreeNode cur, TreeNode pre, int k) {
        if (cur == null) {
            return;
        }
        if (k == 0) {
            ans.add(cur.val);
            return;
        }
        if (cur.left != pre) {
            find(cur.left, cur, k - 1);
        }
        if (cur.right != pre) {
            find(cur.right, cur, k - 1);
        }
        if (parents.get(cur.val) != pre) {
            find(parents.get(cur.val), cur, k - 1);
        }
    }
}
