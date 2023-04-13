package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayDeque;
import java.util.Deque;

/**
 * 662. Maximum Width of Binary Tree
 * https://leetcode.com/problems/maximum-width-of-binary-tree/
 */
public class Problem662 {
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int ans = 1;
        Deque<CustomNode> queue = new ArrayDeque<>();
        queue.add(new CustomNode(0, root));
        while (queue.size() > 0) {
            int n = queue.size();
            int start = 0, end = 0;
            boolean foundFirst = false;
            for (int i = 0; i < n; i++) {
                CustomNode node = queue.pollFirst();
                if (!foundFirst && (node.getLeft() != null || node.getRight() != null)) {
                    foundFirst = true;
                    if (node.getLeft() != null) {
                        start = 2 * node.depth;
                    } else {
                        start = 2 * node.depth + 1;
                    }
                }
                if (node.getLeft() != null) {
                    end = 2 * node.depth;
                }
                if (node.getRight() != null) {
                    end = 2 * node.depth + 1;
                }
                if (node.getLeft() != null) {
                    queue.add(new CustomNode(2 * node.depth, node.getLeft()));
                }
                if (node.getRight() != null) {
                    queue.add(new CustomNode(2 * node.depth + 1, node.getRight()));
                }
            }
            int width = end - start + 1;
            if (width > ans) {
                ans = width;
            }
        }
        return ans;
    }

    static class CustomNode {
        private final int depth;
        private final TreeNode node;

        public CustomNode(int depth, TreeNode node) {
            this.depth = depth;
            this.node = node;
        }

        public TreeNode getLeft() {
            return node.left;
        }

        public TreeNode getRight() {
            return node.right;
        }
    }
}
