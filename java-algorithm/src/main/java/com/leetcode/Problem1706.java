package com.leetcode;

/**
 * 1706. Where Will the Ball Fall
 * https://leetcode.com/problems/where-will-the-ball-fall/
 */
public class Problem1706 {
    public int[] findBall(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            int r = 0, c = i;
            while (r < m) {
                if (grid[r][c] == 1) {
                    if (c == n - 1 || grid[r][c + 1] == -1) {
                        ans[i] = -1;
                        break;
                    }
                    c++;
                } else {
                    if (c == 0 || grid[r][c - 1] == 1) {
                        ans[i] = -1;
                        break;
                    }
                    c--;
                }
                r++;
            }
            if (r == m) {
                ans[i] = c;
            }
        }
        return ans;
    }
}
