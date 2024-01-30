package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 *
 */
public class Problem2808 {
    public int minimumSeconds(List<Integer> nums) {
        Map<Integer, List<Integer>> map = new HashMap<>();
        int n = nums.size(), ans = n;
        for (int i = 0; i < n; i++) {
            map.computeIfAbsent(nums.get(i), k -> new ArrayList<>()).add(i);
        }
        for (List<Integer> positions : map.values()) {
            int max = positions.get(0) + n - positions.get(positions.size() - 1);
            for (int i = 1; i < positions.size(); i++) {
                max = Math.max(max, positions.get(i) - positions.get(i - 1));
            }
            ans = Math.min(ans, max / 2);
        }
        return ans;
    }
}
