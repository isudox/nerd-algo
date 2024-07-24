package com.leetcode;

import java.util.ArrayList;
import java.util.List;
import java.util.TreeMap;

/**
 * 2191. Sort the Jumbled Numbers
 * https://leetcode.com/problems/sort-the-jumbled-numbers/
 */
public class Problem2191 {
    public int[] sortJumbled(int[] mapping, int[] nums) {
        TreeMap<Integer, List<Integer>> map = new TreeMap<>();
        for (int num : nums) {
            int ret = trans(mapping, num);
            List<Integer> list = map.getOrDefault(ret, new ArrayList<>());
            list.add(num);
            map.put(ret, list);
        }
        int[] ans = new int[nums.length];
        int i = 0;
        for (List<Integer> list : map.values()) {
            for (int num : list) {
                ans[i++] = num;
            }
        }
        return ans;
    }

    private int trans(int[] mapping, int num) {
        if (num == 0) {
            return mapping[0];
        }
        StringBuilder sb = new StringBuilder();
        while (num > 0) {
            int digit = num % 10;
            sb.append(mapping[digit]);
            num /= 10;
        }
        sb.reverse();
        return Integer.parseInt(sb.toString());
    }
}
