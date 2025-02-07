package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 3160. Find the Number of Distinct Colors Among the Balls
 * https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/
 */
public class Problem3160 {
    public int[] queryResults(int limit, int[][] queries) {
        int[] ans = new int[queries.length];
        int cur = 0;
        Map<Integer, Integer> balls = new HashMap<>();
        Map<Integer, Integer> count = new HashMap<>();
        for (int i = 0; i < queries.length; i++) {
            int b = queries[i][0], c = queries[i][1];
            int oldColor = balls.getOrDefault(b, 0);
            if (oldColor == c) {
                ans[i] = cur;
                continue;
            }
            if (oldColor > 0) {
                count.put(oldColor, count.get(oldColor) - 1);
                if (count.get(oldColor) == 0) {
                    count.remove(oldColor);
                    cur--;
                }
            }
            balls.put(b, c);
            count.put(c, count.getOrDefault(c, 0) + 1);
            if (count.get(c) == 1) {
                cur++;
            }
            ans[i] = cur;
        }
        return ans;
    }
}
