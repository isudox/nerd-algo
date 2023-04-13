package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * 230. Kth Smallest Element in a BST
 * https://leetcode.com/problems/kth-smallest-element-in-a-bst
 */
public class Problem230 {
    public int kthSmallest(TreeNode root, int k) {
        List<Integer> ret = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        while (!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.add(root);
                root = root.left;
            }
            root = stack.pop();
            ret.add(root.val);
            if (ret.size() == k) {
                return root.val;
            }
            root = root.right;
        }
        return -1;
    }
}
