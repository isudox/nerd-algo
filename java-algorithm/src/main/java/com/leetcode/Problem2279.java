package com.leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/**
 * 2279. Maximum Bags With Full Capacity of Rocks
 * https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
 */
public class Problem2279 {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int ans = 0;
        Map<Integer, List<Integer>> map = new TreeMap<>();
        for (int i = 0; i < capacity.length; i++) {
            int d = capacity[i] - rocks[i];
            if (d == 0) {
                ans++;
                continue;
            }
            List<Integer> idx = map.getOrDefault(d, new ArrayList<>());
            idx.add(i);
            map.put(d, idx);
        }
        for (Map.Entry<Integer, List<Integer>> entry : map.entrySet()) {
            int d = entry.getKey();
            List<Integer> idx = entry.getValue();
            int cnt = Math.min(idx.size(), additionalRocks / d);
            ans += cnt;
            additionalRocks -= cnt * d;
            if (additionalRocks <= 0) {
                break;
            }
        }
        return ans;
    }
}
