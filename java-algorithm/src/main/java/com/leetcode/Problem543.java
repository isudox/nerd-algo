package com.leetcode;

import com.common.TreeNode;

import java.util.HashMap;
import java.util.Map;

/**
 * 543. Diameter of Binary Tree
 * https://leetcode.com/problems/diameter-of-binary-tree/
 *
 * Given a binary tree, you need to compute the length of the diameter of the tree.
 * The diameter of a binary tree is the length of the longest path between
 * any two nodes in a tree. This path may or may not pass through the root.
 *
 * Example:
 * Given a binary tree
 *           1
 *          / \
 *         2   3
 *        / \
 *       4   5
 * Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
 *
 * Note:
 *
 * The length of path between two nodes is represented by the number of
 * edges between them.
 */
public class Problem543 {

    private Map<TreeNode, int[]> memo = new HashMap<>();
    private int ans = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        recur(root);
        return ans;
    }

    private int[] recur(TreeNode node) {
        if (null == node)
            return new int[]{2, 2};
        if (memo.containsKey(node))
            return memo.get(node);
        int curL = 0, curR = 0;
        if (null != node.left) {
            int[] left = recur(node.left);
            curL = Math.max(left[0], left[1]) + 1;
        }
        if (null != node.right) {
            int[] right = recur(node.right);
            curR = Math.max(right[0], right[1]) + 1;
        }
        memo.put(node, new int[]{curL, curR});
        ans = Math.max(ans, curL + curR);
        return memo.get(node);
    }
}
