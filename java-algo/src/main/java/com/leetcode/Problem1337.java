package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 1337. The K Weakest Rows in a Matrix
 * https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
 */
public class Problem1337 {
    public int[] kWeakestRows(int[][] mat, int k) {
        int m = mat.length, n = mat[0].length;
        Map<Integer, List<Integer>> store = new HashMap<>();
        for (int i = 0; i < m; i++) {
            int cur = 0;
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    break;
                }
                cur++;
            }
            List<Integer> list = store.getOrDefault(cur, new ArrayList<>());
            list.add(i);
            store.put(cur, list);
        }
        int[] ans = new int[k];
        int x = 0;
        for (int i = 0; i <= n; i++) {
            List<Integer> list = store.getOrDefault(i, new ArrayList<>());
            for (Integer pos : list) {
                ans[x++] = pos;
                if (x == k) {
                    return ans;
                }
            }
        }
        return ans;
    }
}
