package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 1609. Even Odd Tree
 * https://leetcode.com/problems/even-odd-tree/
 */
public class Problem1609 {
    public boolean isEvenOddTree(TreeNode root) {
        Deque<TreeNode> q = new ArrayDeque<>();
        q.push(root);
        boolean flag = false;
        while (!q.isEmpty()) {
            int n = q.size();
            int pre = -1;
            for (int i = 0; i < n; i++) {
                TreeNode node = q.pollFirst();
                int cur = node.val;
                if (flag && cur % 2 == 1) {
                    return false;
                }
                if (!flag && cur % 2 == 0) {
                    return false;
                }
                if (i > 0) {
                    if (flag && cur >= pre) {
                        return false;
                    }
                    if (!flag && cur <= pre) {
                        return false;
                    }
                }
                if (node.left != null) {
                    q.offerLast(node.left);
                }
                if (node.right != null) {
                    q.offerLast(node.right);
                }
                pre = cur;
            }
            flag = !flag;
        }
        return true;
    }
}
