package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

/**
 * 144. Binary Tree Preorder Traversal
 * https://leetcode.com/problems/binary-tree-preorder-traversal/
 */
public class Problem144 {
    /**
     * Recursion
     */
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null)
            return ans;
        ans.add(root.val);
        if (root.left != null)
            ans.addAll(preorderTraversal(root.left));
        if (root.right != null)
            ans.addAll(preorderTraversal(root.right));
        return ans;
    }

    /**
     * Iteration.
     */
    public List<Integer> preorderTraversal2(TreeNode root) {
        List<Integer> ans = new ArrayList<>();
        if (root == null)
            return ans;
        Deque<TreeNode> deque = new LinkedList<>();
        deque.offer(root);
        while (!deque.isEmpty()) {
            TreeNode node = deque.pollFirst();
            ans.add(node.val);
            if (node.right != null)
                deque.offerFirst(node.right);
            if (node.left != null)
                deque.offerFirst(node.left);
        }
        return ans;
    }
}
