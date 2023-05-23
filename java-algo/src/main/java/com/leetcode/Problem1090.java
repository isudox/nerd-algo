package com.leetcode;

import java.util.*;

/**
 * 1090. Largest Values From Labels
 * https://leetcode.com/problems/largest-values-from-labels/
 */
public class Problem1090 {
    public int largestValsFromLabels(int[] values, int[] labels, int numWanted, int useLimit) {
        int[][] pairs = new int[values.length][2];
        for (int i = 0; i < values.length; i++) {
            pairs[i][0] = values[i];
            pairs[i][1] = labels[i];
        }
        Arrays.sort(pairs, (o1, o2) -> o2[0] - o1[0]);
        int ans = 0, cnt = 0;
        Map<Integer, Integer> counter = new HashMap<>();
        for (int[] pair : pairs) {
            int val = pair[0], label = pair[1];
            if (counter.getOrDefault(label, 0) < useLimit) {
                counter.put(label, counter.getOrDefault(label, 0) + 1);
                ans += val;
                if (++cnt == numWanted) {
                    break;
                }
            }
        }
        return ans;
    }
}
