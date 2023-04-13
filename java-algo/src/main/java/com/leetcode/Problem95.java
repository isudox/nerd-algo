package com.leetcode;

import com.common.TreeNode;

import java.util.*;

/**
 * 95. Unique Binary Search Trees II
 * https://leetcode.com/problems/unique-binary-search-trees-ii/
 *
 * Given an integer n, generate all structurally unique BST's (binary search trees)
 * that store values 1 ... n.
 *
 * Example:
 *
 * Input: 3
 * Output:
 * [
 *   [1,null,3,2],
 *   [3,2,null,1],
 *   [3,1,null,null,2],
 *   [2,1,3],
 *   [1,null,2,null,3]
 * ]
 * Explanation:
 * The above output corresponds to the 5 unique BST's shown below:
 *
 *    1         3     3      2      1
 *     \       /     /      / \      \
 *      3     2     1      1   3      2
 *     /     /       \                 \
 *    2     1         2                 3
 *
 *
 * Constraints:
 *
 * 0 <= n <= 8
 */
public class Problem95 {

    public List<TreeNode> generateTrees(int n) {
        if (n==0)
            return Collections.emptyList();
        return recur(1, n);
    }

    private List<TreeNode> recur(int left, int right) {
        List<TreeNode> ret = new ArrayList<>();
        if (left > right) {
            ret.add(null);
            return ret;
        }
        if (left == right) {
            ret.add(new TreeNode(left));
            return ret;
        }
        for (int i = left; i <= right; i++) {
            List<TreeNode> l = recur(left, i - 1);
            List<TreeNode> r = recur(i + 1, right);
            for (TreeNode leftNode : l) {
                for (TreeNode rightNode : r) {
                    TreeNode root = new TreeNode(i);
                    root.left = leftNode;
                    root.right = rightNode;
                    ret.add(root);
                }
            }
        }
        return ret;
    }

    public List<TreeNode> generateTrees2(int n) {
        if (n == 0)
            return Collections.emptyList();
        Map<String, List<TreeNode>> memo = new HashMap<>();
        return recurWithMemo(1, n, memo);
    }

    private List<TreeNode> recurWithMemo(int left, int right, Map<String, List<TreeNode>> memo) {
        String key = "" + left + "-" + right;
        if (memo.containsKey(key))
            return memo.get(key);
        List<TreeNode> ret = new ArrayList<>();
        if (left > right) {
            ret.add(null);
            return ret;
        }
        if (left == right) {
            ret.add(new TreeNode(left));
            return ret;
        }
        for (int i = left; i <= right; i++) {
            List<TreeNode> l = recurWithMemo(left, i - 1, memo);
            List<TreeNode> r = recurWithMemo(i + 1, right, memo);
            for (TreeNode leftNode : l) {
                for (TreeNode rightNode : r) {
                    TreeNode root = new TreeNode(i);
                    root.left = leftNode;
                    root.right = rightNode;
                    ret.add(root);
                }
            }
        }
        memo.put(key, ret);
        return ret;
    }

}
