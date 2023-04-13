package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1630. Arithmetic Subarrays
 */
public class Problem1630 {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        List<Boolean> ans = new ArrayList<>();
        for (int i = 0; i < l.length; i++) {
            int left = l[i], right = r[i];
            int min = nums[left], max = nums[left];
            for (int j = left; j <= right; j++) {
                min = Math.min(min, nums[j]);
                max = Math.max(max, nums[j]);
            }
            if (min == max) {
                ans.add(true);
                continue;
            }
            if ((max - min) % (right - left) > 0) {
                ans.add(false);
                continue;
            }
            int d = (max - min) / (right - left);
            boolean[] seen = new boolean[right - left + 1];
            boolean flag = true;
            for (int j = left; j <= right; j++) {
                if ((nums[j] - min) % d != 0) {
                    flag = false;
                    break;
                }
                int x = (nums[j] - min) / d;
                if (seen[x]) {
                    flag = false;
                    break;
                }
                seen[x] = true;
            }
            ans.add(flag);
        }
        return ans;
    }
}
