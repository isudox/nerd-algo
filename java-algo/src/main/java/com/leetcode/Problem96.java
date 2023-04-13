package com.leetcode;

/**
 * 96. Unique Binary Search Trees
 * https://leetcode.com/problems/unique-binary-search-trees/
 *
 * Given n, how many structurally unique BST's that store values 1 ... n?
 *
 * Example:
 *
 * Input: 3
 * Output: 5
 * Explanation:
 * Given n = 3, there are a total of 5 unique BST's:
 *
 *    1         3     3      2      1
 *     \       /     /      / \      \
 *      3     2     1      1   3      2
 *     /     /       \                 \
 *    2     1         2                 3
 */
public class Problem96 {
    public int numTrees(int n) {
        // dp[i][j] means (1 ... n) BST which parent node is j.
        int[][] dp = new int[n + 1][n + 1];
        dp[0][0] = 1;
        dp[1][1] = 1;
        for (int i = 2; i < n + 1; i++) {
            for (int j = 1; j <= i; j++) {
                if (j == 1) {
                    dp[i][j] = sumArray(dp[i - 1]);
                } else if (j == i) {
                    dp[i][j] = sumArray(dp[i - 1]);
                } else {
                    dp[i][j] = sumArray(dp[j - 1]) * sumArray(dp[i - j]);
                }
            }
        }
        return sumArray(dp[n]);
    }

    private int sumArray(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return sum;
    }

    public int numTrees2(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] += dp[i - 1] * 2;
            for (int j = 2; j < i; j++) {
                dp[i] += dp[j - 1] * dp[i - j];
            }
        }
        return dp[n];
    }

}
