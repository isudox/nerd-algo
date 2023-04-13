package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 279. Perfect Squares
 * https://leetcode.com/problems/perfect-squares/
 */
public class Problem279 {

    /**
     * Greedy
     * Time Complexity:
     * Space Complexity:
     */
    public int numSquares(int n) {
        return recur(n, new int[n + 1]);
    }

    private int recur(int m, int[] memo) {
        if (memo[m] != 0)
            return memo[m];
        int start = (int) Math.sqrt(m);
        int ret = m;
        while (start > 0) {
            ret = Math.min(ret, 1 + recur(m - start * start, memo));
            start--;
        }
        memo[m] = ret;
        return ret;
    }

    public int numSquares2(int n) {
        int[] dp = new int[n + 1];
        List<Integer> squares = initSquares(n);
        for (int i = 1; i <= n; i++) {
            dp[i] = n;
            for (int square : squares) {
                if (square > i) break;
                dp[i] = Math.min(dp[i], dp[i - square] + 1);
            }
        }
        return dp[n];
    }

    private List<Integer> initSquares(int m) {
        List<Integer> squares = new ArrayList<>();
        int prev = 0;
        int i = 0;
        while (prev < m) {
            prev += (i++ << 1) + 1;
            squares.add(prev);
        }
        return squares;
    }

    public int numSquares3(int n) {
        List<Integer> squares = initSquares(n);
        for (int i = 1; i < n + 1; i++)
            if (canDivide(n, i, squares))
                return i;
        return n;
    }

    private boolean canDivide(int n, int k, List<Integer> squares) {
        if (k == 1)
            return squares.contains(n);
        for (int square : squares)
            if (canDivide(n - square, k - 1, squares))
                return true;
        return false;
    }

    public int numSquares4(int n) {
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            dp[i] = i;
            for (int j = (int) Math.sqrt(i); j > 0; j--) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }
        return dp[n];
    }
}
