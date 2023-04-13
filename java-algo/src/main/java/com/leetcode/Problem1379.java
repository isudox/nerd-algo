package com.leetcode;

import com.common.TreeNode;

/**
 * 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
 * https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
 */
public class Problem1379 {
    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        if (cloned.val == target.val) {
            return cloned;
        }
        TreeNode ans = null;
        if (cloned.left != null) {
            ans = getTargetCopy(original, cloned.left, target);
        }
        if (ans != null) {
            return ans;
        }
        if (cloned.right != null) {
            ans = getTargetCopy(original, cloned.right, target);
        }
        return ans;
    }
}
