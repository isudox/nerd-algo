package com.leetcode;

import java.util.List;

/**
 * 120. Triangle
 * https://leetcode.com/problems/triangle/
 *
 * Given a triangle, find the minimum path sum from top to bottom.
 * Each step you may move to adjacent numbers on the row below.
 *
 * For example, given the following triangle
 *
 * [
 *      [2],
 *     [3,4],
 *    [6,5,7],
 *   [4,1,8,3]
 * ]
 *
 * The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
 *
 * Note:
 *
 * Bonus point if you are able to do this using only O(n) extra space,
 * where n is the total number of rows in the triangle.
 *
 * Constraints:
 *
 * 1 <= triangle.length <= 200
 * triangle[0].length == 1
 * triangle[i].length == triangle[i - 1].length + 1
 * -10^4 <= triangle[i][j] <= 10^4
 */
public class Problem120 {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        return dfs(triangle, 0, 0, new Integer[n][n]);
    }

    private int dfs(List<List<Integer>> t, int r, int c, Integer[][] memo) {
        if (r == memo.length - 1) {
            return t.get(r).get(c);
        }
        if (memo[r][c] != null) {
            return memo[r][c];
        }
        int ret = Math.min(dfs(t, r + 1, c, memo), dfs(t, r + 1, c + 1, memo));
        return memo[r][c] = ret + t.get(r).get(c);
    }
}
