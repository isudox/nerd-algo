package com.leetcode;

import com.common.TreeNode;

/**
 * 1457. Pseudo-Palindromic Paths in a Binary Tree
 * https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
 */
public class Problem1457 {
    private int ans = 0;
    public int pseudoPalindromicPaths (TreeNode root) {
        dfs(root, new int[10]);
        return ans;
    }

    private void dfs(TreeNode node, int[] counter) {
        counter[node.val] += 1;
        if (node.left == null && node.right == null) {
            if (check(counter))
                ans++;
        }
        if (node.left != null) {
            dfs(node.left, counter);
        }
        if (node.right != null) {
            dfs(node.right, counter);
        }
        counter[node.val] -= 1;
    }

    private boolean check(int[] counter) {
        int odds = 0;
        for (int i = 0; i < 10; i++) {
            if (counter[i] % 2 == 1) {
                if (++odds > 1)
                    return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Problem1457 sol = new Problem1457();
        TreeNode root = new TreeNode(1, null, new TreeNode(2));
        System.out.println(sol.pseudoPalindromicPaths(root));
    }
}
