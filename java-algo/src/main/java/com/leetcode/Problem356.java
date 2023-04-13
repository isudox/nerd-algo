package com.leetcode;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * 356. Line Reflection
 * https://leetcode.com/problems/line-reflection/
 */
public class Problem356 {
    public boolean isReflected(int[][] points) {
        Map<Integer, Set<Integer>> group = new HashMap<>();
        int min = 100000000, max = -100000000;
        for (int[] point : points) {
            int x = point[0], y = point[1];
            min = Math.min(min, x);
            max = Math.max(max, x);
            if (group.containsKey(y)) {
                group.get(y).add(x);
            } else {
                Set<Integer> set = new HashSet<>();
                set.add(x);
                group.put(y, set);
            }
        }
        int sum = min + max;
        for (Map.Entry<Integer, Set<Integer>> entry : group.entrySet()) {
            Set<Integer> xSet = entry.getValue();
            for (int x : xSet) {
                if (!xSet.contains(sum - x))
                    return false;
            }
        }
        return true;
    }
}
