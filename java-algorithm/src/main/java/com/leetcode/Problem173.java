package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * 173. Binary Search Tree Iterator
 * https://leetcode.com/problems/binary-search-tree-iterator/
 */
public class Problem173 {
    private static class BSTIterator {
        private List<Integer> list = new ArrayList<>();
        private int index = 0;

        public BSTIterator(TreeNode root) {
            dfs(root);
        }

        public int next() {
            return list.get(index++);
        }

        public boolean hasNext() {
            return index < list.size();
        }

        private void dfs(TreeNode node) {
            if (node == null) {
                return;
            }
            dfs(node.left);
            list.add(node.val);
            dfs(node.right);
        }
    }

}
