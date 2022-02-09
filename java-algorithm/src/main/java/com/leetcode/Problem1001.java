package com.leetcode;

import java.util.*;

/**
 * 1001. Grid Illumination
 * https://leetcode.com/problems/grid-illumination/
 */
public class Problem1001 {
    public int[] gridIllumination(int n, int[][] lamps, int[][] queries) {
        Map<Integer, Integer> rowCnt = new HashMap<>();
        Map<Integer, Integer> colCnt = new HashMap<>();
        Map<Integer, Integer> diaCnt1 = new HashMap<>();
        Map<Integer, Integer> diaCnt2 = new HashMap<>();
        Set<String> lighted = new HashSet<>();
        for (int[] lamp : lamps) {
            int r = lamp[0], c = lamp[1];
            String key = String.format("%d-%d", r, c);
            if (!lighted.contains(key)) {
                lighted.add(key);
                rowCnt.put(r, rowCnt.getOrDefault(r, 0) + 1);
                colCnt.put(c, colCnt.getOrDefault(c, 0) + 1);
                diaCnt1.put(r + c, diaCnt1.getOrDefault(r + c, 0) + 1);
                diaCnt2.put(r - c, diaCnt2.getOrDefault(r - c, 0) + 1);
            }
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int r = queries[i][0], c = queries[i][1];
            if (rowCnt.getOrDefault(r, 0) > 0 ||
                    colCnt.getOrDefault(c, 0) > 0 ||
                    diaCnt1.getOrDefault(r + c, 0) > 0 ||
                    diaCnt2.getOrDefault(r - c, 0) > 0) {
                ans[i] = 1;
            }
            for (int x = r - 1; x <= r + 1; x++) {
                for (int y = c - 1; y <= c + 1; y++) {
                    String key = String.format("%d-%d", x, y);
                    if (0 <= x && x < n && 0 <= y && y < n && lighted.contains(key)) {
                        lighted.remove(key);
                        rowCnt.put(x, rowCnt.get(x) - 1);
                        colCnt.put(y, colCnt.get(y) - 1);
                        diaCnt1.put(x + y, diaCnt1.get(x + y) - 1);
                        diaCnt2.put(x - y, diaCnt2.get(x - y) - 1);
                    }
                }
            }
        }
        return ans;
    }
}
