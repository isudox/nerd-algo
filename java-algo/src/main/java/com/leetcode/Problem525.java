package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 525. Contiguous Array
 * https://leetcode.com/problems/contiguous-array/
 */
public class Problem525 {
    public int findMaxLength(int[] nums) {
        Map<Integer, Integer> diff = new HashMap<>();
        diff.put(0, -1);
        int[] cnt = new int[2];
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            cnt[nums[i]]++;
            int d = cnt[1] - cnt[0];
            if (diff.containsKey(d)) {
                ans = Math.max(ans, i - diff.get(d));
            } else {
                diff.put(d, i);
            }
        }
        return ans;
    }
}
