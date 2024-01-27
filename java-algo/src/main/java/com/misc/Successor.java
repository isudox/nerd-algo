package com.misc;

import com.common.TreeNode;

import java.util.*;

/**
 * 04.06. Successor LCCI
 * https://leetcode.com/problems/successor-lcci/
 */
public class Successor {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        TreeNode pre = null, cur = root;
        while (!stack.isEmpty() || cur != null) {
            while (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            if (pre == p) {
                return cur;
            }
            pre = cur;
            cur = cur.right;
        }
        return null;
    }
    public TreeNode inorderSuccessor2(TreeNode root, TreeNode p) {
        if (root == null) {
            return null;
        }
        if (root.val <= p.val) {
            return inorderSuccessor2(root.right, p);
        }
        TreeNode ans = inorderSuccessor2(root.left, p);
        return ans;
    }
}
