package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * """254. Factor Combinations
 * https://leetcode-cn.com/problems/factor-combinations
 *
 * Numbers can be regarded as the product of their factors.
 *
 * For example, 8 = 2 x 2 x 2 = 2 x 4.
 * Given an integer n, return all possible combinations of its factors.
 * You may return the answer in any order.
 *
 * Note that the factors should be in the range [2, n - 1].
 *
 * Example 1:
 * Input: n = 1
 * Output: []
 *
 * Example 2:
 * Input: n = 12
 * Output: [[2,6],[3,4],[2,2,3]]
 *
 * Example 3:
 * Input: n = 37
 * Output: []
 *
 * Example 4:
 * Input: n = 32
 * Output: [[2,16],[4,8],[2,2,8],[2,4,4],[2,2,2,4],[2,2,2,2,2]]
 *
 * Constraints:
 *
 * 1 <= n <= 10^8
 */
public class Problem254 {
    public List<List<Integer>> getFactors(int n) {
        List<List<Integer>> ans = new ArrayList<>();
        dfs(2, n, 1, ans, new ArrayList<>());
        return ans;
    }

    private void dfs(int start, int n, int production, List<List<Integer>> ans, List<Integer> cur) {
        if (start >= n || production > n)
            return;
        if (production == n) {
            ans.add(new ArrayList<>(cur));
            return;
        }
        for (int i = start, k = n / production; i <= k; i++) {
            if (n % i == 0) {
                cur.add(i);
                dfs(i, n, production * i, ans, cur);
                cur.remove(cur.size() - 1);
            }
        }
    }
}
