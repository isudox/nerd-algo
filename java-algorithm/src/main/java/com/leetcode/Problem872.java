package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.List;
import java.util.zip.CRC32;
import java.util.zip.Checksum;

/**
 * 872. Leaf-Similar Trees
 * https://leetcode.com/problems/leaf-similar-trees/
 *
 * Consider all the leaves of a binary tree, from left to right order, the
 * values of those leaves form a leaf value sequence.
 *
 * For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
 * 8).
 *
 * Two binary trees are considered leaf-similar if their leaf value sequence is
 * the same.
 *
 * Return true if and only if the two given trees with head nodes root1 and
 * root2 are leaf-similar.
 *
 * Example 1:
 *
 * Input: root1 = [3,5,1,6,2,9,8,null,null,7,4],
 * root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
 * Output: true
 *
 * Example 2:
 *
 * Input: root1 = [1], root2 = [1]
 * Output: true
 *
 * Example 3:
 *
 * Input: root1 = [1], root2 = [2]
 * Output: false
 *
 * Example 4:
 *
 * Input: root1 = [1,2], root2 = [2,2]
 * Output: true
 *
 * Example 5:
 *
 * Input: root1 = [1,2,3], root2 = [1,3,2]
 * Output: false
 *
 * Constraints:
 *
 * The number of nodes in each tree will be in the range [1, 200].
 * Both of the given trees will have values in the range [0, 200].
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
