package com.leetcode;

import com.common.TreeNode;

import java.sql.Array;
import java.util.ArrayList;
import java.util.List;

/**
 * 919. Complete Binary Tree Inserter
 * https://leetcode.com/problems/complete-binary-tree-inserter/
 */
public class Problem919 {
    private static class CBTInserter {
        private final TreeNode root;
        private final List<TreeNode> level;
        private int index;

        public CBTInserter(TreeNode root) {
            this.root = root;
            this.level = new ArrayList<>();
            List<TreeNode> nextLevel = new ArrayList<>();
            level.add(root);
            while (!level.isEmpty()) {
                for (TreeNode node : level) {
                    if (node.left != null) nextLevel.add(node.left);
                    else return;
                    if (node.right != null) nextLevel.add(node.right);
                    else return;
                    index++;
                }
                level.clear();
                level.addAll(nextLevel);
                nextLevel.clear();
                index = 0;
            }
        }

        public int insert(int val) {
            TreeNode par = level.get(index), node = new TreeNode(val);
            if (par.left == null) par.left = node;
            else if (par.right == null) par.right = node;
            else if (index < level.size() - 1) {
                index++;
                level.get(index).left = node;
            } else {
                int n = level.size();
                for (int i = 0; i < n; i++) {
                    TreeNode tmp = level.remove(0);
                    level.add(tmp.left);
                    level.add(tmp.right);
                }
                index = 0;
                level.get(index).left = node;
            }
            return level.get(index).val;
        }

        public TreeNode get_root() {
            return this.root;
        }
    }
}
