package com.misc;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * 04.06. Successor LCCI
 * https://leetcode.cn/problems/successor-lcci/
 */
public class Successor {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        Stack<TreeNode> stack = new Stack<>();
        List<TreeNode> list = new ArrayList<>();
        while (!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.add(root);
                root = root.left;
            }
            root = stack.pop();
            list.add(root);
            root = root.right;
        }
        for (int i = 1; i < list.size(); i++) {
            if (list.get(i - 1) == p) {
                return list.get(i);
            }
        }
        return null;
    }
}
