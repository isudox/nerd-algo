package com.leetcode;

import java.util.*;

/**
 * 2225. Find Players With Zero or One Losses
 * https://leetcode.com/problems/find-players-with-zero-or-one-losses/
 */
public class Problem2225 {
    public List<List<Integer>> findWinners(int[][] matches) {
        Map<Integer, int[]> map = new HashMap<>();
        for (int[] m : matches) {
            int[] count0 = map.getOrDefault(m[0], new int[2]);
            count0[0]++;
            map.put(m[0], count0);
            int[] count1 = map.getOrDefault(m[1], new int[2]);
            count1[1]++;
            map.put(m[1], count1);
        }
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(list1);
        ans.add(list2);
        for (Map.Entry<Integer, int[]> entry : map.entrySet()) {
            int p = entry.getKey();
            int w = entry.getValue()[0], l = entry.getValue()[1];
            if (w > 0 && l == 0) {
                list1.add(p);
            }
            if (l == 1) {
                list2.add(p);
            }
        }
        list1.sort(Comparator.comparingInt(o -> o));
        list2.sort(Comparator.comparingInt(o -> o));
        return ans;
    }
}
