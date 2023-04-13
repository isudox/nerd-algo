package com.leetcode;

import com.common.TreeNode;

/**
 * 108. Convert Sorted Array to Binary Search Tree
 * https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
 *
 * Given an array where elements are sorted in ascending order,
 * convert it to a height balanced BST.
 *
 * For this problem, a height-balanced binary tree is defined as a binary tree in
 * which the depth of the two subtrees of every node never differ by more than 1.
 *
 * Example:
 *
 * Given the sorted array: [-10,-3,0,5,9],
 *
 * One possible answer is: [0,-3,9,-10,null,5],
 * which represents the following height balanced BST:
 *
 *       0
 *      / \
 *    -3   9
 *    /   /
 *  -10  5
 */
public class Problem108 {

    public TreeNode sortedArrayToBST(int[] nums) {
        return recur(nums, 0, nums.length);
    }

    private TreeNode recur(int[] nums, int start, int end) {
        // [start, end)
        if (end - start == 0)
            return null;
        int mid = (start + end) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = recur(nums, start, mid);
        root.right = recur(nums, mid + 1, end);
        return root;
    }
}
