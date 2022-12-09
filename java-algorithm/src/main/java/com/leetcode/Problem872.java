package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.zip.CRC32;
import java.util.zip.Checksum;

/**
 * 872. Leaf-Similar Trees
 * https://leetcode.com/problems/leaf-similar-trees/
 */
public class Problem872 {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leaf1 = new ArrayList<>();
        List<Integer> leaf2 = new ArrayList<>();
        helper(root1, leaf1);
        helper(root2, leaf2);
        return leaf1.equals(leaf2);
    }

    private void helper(TreeNode node, List<Integer> leaf) {
        if (null == node)
            return;
        if (null == node.left && null == node.right) {
            leaf.add(node.val);
            return;
        }
        helper(node.left, leaf);
        helper(node.right, leaf);
    }

    public boolean leafSimilar2(TreeNode root1, TreeNode root2) {
        Checksum checksum1 = new CRC32(), checksum2 = new CRC32();
        checksum(root1, checksum1);
        checksum(root2, checksum2);
        return checksum1.getValue() == checksum2.getValue();
    }
    private void checksum(TreeNode node, Checksum crc32) {
        if (null == node)
            return;
        if (null == node.left && null == node.right) {
            crc32.update(node.val);
            return;
        }
        checksum(node.left, crc32);
        checksum(node.right, crc32);
    }
}
