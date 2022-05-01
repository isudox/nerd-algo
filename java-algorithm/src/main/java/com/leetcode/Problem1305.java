package com.leetcode;

import com.common.TreeNode;

import java.util.*;

/**
 * 1305. All Elements in Two Binary Search Trees
 * https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
 */
public class Problem1305 {
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> list1 = helper(root1);
        List<Integer> list2 = helper(root2);
        if (list1.isEmpty()) {
            return list2;
        }
        if (list2.isEmpty()) {
            return list1;
        }
        int i = 0, j = 0;
        List<Integer> ans = new ArrayList<>();
        while (i < list1.size() && j < list2.size()) {
            if (list1.get(i) < list2.get(j)) {
                ans.add(list1.get(i++));
            } else {
                ans.add(list2.get(j++));
            }
        }
        while (i < list1.size()) {
            ans.add(list1.get(i++));
        }
        while (j < list2.size()) {
            ans.add(list2.get(j++));
        }
        return ans;
    }

    private List<Integer> helper(TreeNode node) {
        List<Integer> list = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        if (node == null) {
            return list;
        }
        while (!stack.isEmpty() || node != null) {
            while (node != null) {
                stack.add(node);
                node = node.left;
            }
            node = stack.pop();
            list.add(node.val);
            node = node.right;
        }
        return list;
    }
}
