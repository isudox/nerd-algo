package com.leetcode;

/**
 * 835. Image Overlap
 * https://leetcode.com/problems/image-overlap/
 */
public class Problem835 {
    public int largestOverlap(int[][] img1, int[][] img2) {
        int N = img1.length;
        int[][] count = new int[2 * N + 1][2 * N + 1];
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                if (img1[i][j] == 1) {
                    for (int i2 = 0; i2 < N; ++i2) {
                        for (int j2 = 0; j2 < N; ++j2) {
                            if (img2[i2][j2] == 1) {
                                count[i - i2 + N][j - j2 + N] += 1;
                            }
                        }
                    }
                }
            }
        }
        int ans = 0;
        for (int[] row : count) {
            for (int v : row) {
                ans = Math.max(ans, v);
            }
        }
        return ans;
    }
}
