package com.leetcode;

import com.common.TreeNode;

/**
 * 654. Maximum Binary Tree
 * https://leetcode.com/problems/maximum-binary-tree/
 */
class Problem654 {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return recur(nums, 0, nums.length);
    }

    private TreeNode recur(int[] nums, int start, int end) {
        if (start == end) return null;
        int pos = start, max = nums[start];
        for (int i = start; i < end; i++) {
            if (nums[i] > max) {
                max = nums[i];
                pos = i;
            }
        }
        TreeNode root = new TreeNode(nums[pos]);
        root.left = recur(nums, start, pos);
        root.right = recur(nums, pos + 1, end);
        return root;
    }
}

