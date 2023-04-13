package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * 938. Range Sum of BST
 * https://leetcode.com/problems/range-sum-of-bst/
 *
 * Given the root node of a binary search tree, return the sum of values of
 * all nodes with value between Low and High (inclusive).
 *
 * The binary search tree is guaranteed to have unique values.
 *
 * Example 1:
 *
 * Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
 * Output: 32
 *
 * Example 2:
 *
 * Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
 * Output: 23
 *
 * Note:
 *
 * The number of nodes in the tree is at most 10000.
 * The final answer is guaranteed to be less than 2^31.
 */
public class Problem938 {
    public int rangeSumBST1(TreeNode root, int low, int high) {
        if (root == null)
            return 0;
        int ans = 0;
        List<TreeNode> queue = new ArrayList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.remove(0);
            if (node == null)
                continue;
            if (node.val < low) {
                queue.add(node.right);
            } else if (node.val > high) {
                queue.add(node.left);
            } else {
                ans += node.val;
                queue.add(node.left);
                queue.add(node.right);
            }
        }
        return ans;
    }

    public int rangeSumBST(TreeNode root, int low, int high) {
        int ans = 0;
        List<TreeNode> stack = new ArrayList<>();
        while (root != null || !stack.isEmpty()) {
            if (root != null) {
                stack.add(root);
                root = root.left;
            } else {
                root = stack.remove(stack.size() - 1);
                if (root.val <= high && root.val >= low)
                    ans += root.val;
                if (root.val > high)
                    break;
                root = root.right;
            }
        }
        return ans;
    }

    public int rangeSumBST2(TreeNode root, int low, int high) {
        if (root == null)
            return 0;
        int ans = 0;
        if (root.val <= high && root.val >= low) {
            ans += root.val;
            ans += rangeSumBST2(root.left, low, high);
            ans += rangeSumBST2(root.right, low, high);
        } else if (root.val < low) {
            ans += rangeSumBST2(root.right, low, high);
        } else {
            ans += rangeSumBST2(root.left, low, high);
        }
        return ans;
    }
}
