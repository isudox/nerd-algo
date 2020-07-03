package com.leetcode;

import com.common.TreeNode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;

/**
 * 971. Flip Binary Tree To Match Preorder Traversal
 * https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
 * Given a binary tree with N nodes, each node has a different value from
 * {1, ..., N}.
 * <p>
 * A node in this binary tree can be flipped by swapping the left child and the
 * right child of that node.
 * <p>
 * Consider the sequence of N values reported by a preorder traversal starting from
 * the root.  Call such a sequence of N values the voyage of the tree.
 * <p>
 * (Recall that a preorder traversal of a node means we report the current
 * node's value, then preorder-traverse the left child, then preorder-traverse the
 * right child.)
 * <p>
 * Our goal is to flip the least number of nodes in the tree so that the voyage of
 * the tree matches the voyage we are given.
 * <p>
 * If we can do so, then return a list of the values of all nodes flipped.  You may
 * return the answer in any order.
 * <p>
 * If we cannot do so, then return the list [-1].
 * <p>
 * Example 1:
 * Input: root = [1,2], voyage = [2,1]
 * Output: [-1]
 * <p>
 * Example 2:
 * Input: root = [1,2,3], voyage = [1,3,2]
 * Output: [1]
 * <p>
 * Example 3:
 * Input: root = [1,2,3], voyage = [1,2,3]
 * Output: []
 * <p>
 * Note:
 * 1 <= N <= 100
 */
public class Problem971 {

    public List<Integer> flipMatchVoyage(TreeNode root, int[] voyage) {
        int size = voyage.length;
        int i = 0;
        List<Integer> ans = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);

        while (!stack.isEmpty() && i < size) {
            TreeNode temp = stack.pop();
            if (temp.val != voyage[i])
                break;
            i++;
            if (i < size) {
                if (temp.left != null && temp.left.val != voyage[i]) {
                    ans.add(temp.val);
                    stack.push(temp.left);
                    if (temp.right != null) {
                        stack.push(temp.right);
                    }
                } else {
                    if (temp.right != null) {
                        stack.push(temp.right);
                    }
                    if (temp.left != null) {
                        stack.push(temp.left);
                    }
                }
            }
        }

        return i == size ? ans : Collections.singletonList(-1);
    }
}
