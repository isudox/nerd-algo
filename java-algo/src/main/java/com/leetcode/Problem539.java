package com.leetcode;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * 539. Minimum Time Difference
 * https://leetcode.com/problems/minimum-time-difference/
 */
public class Problem539 {
    public int findMinDifference(List<String> timePoints) {
        List<Integer> list = new ArrayList<>();
        for (String point : timePoints) {
            String[] segs = point.split(":");
            list.add(Integer.parseInt(segs[0]) * 60 + Integer.parseInt(segs[1]));
        }
        Collections.sort(list);
        int ans = 24 * 60;
        for (int i = 0; i < list.size(); i++) {
            int diff = Math.abs(list.get((i + 1) % list.size()) - list.get(i));
            ans = Math.min(ans, Math.min(diff, 1440 - diff));
        }
        return ans;
    }
}
