package com.leetcode;

import java.util.*;

/**
 * 2597. The Number of Beautiful Subsets
 * https://leetcode.com/problems/the-number-of-beautiful-subsets/
 */
public class Problem2597 {
    public int beautifulSubsets(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int limit = 1 << n;
        int ans = 0;
        for (int i = 1; i < limit; i++) {
            int x = i;
            List<Integer> list = new ArrayList<>();
            for (int num : nums) {
                if ((x & 1) == 1) {
                    list.add(num);
                }
                x >>= 1;
            }
            ans += check(list, k);
        }
        return ans;
    }

    private int check(List<Integer> list, int k) {
        Set<Integer> seen = new HashSet<>();
        for (int num : list) {
            if (seen.contains(num - k)) {
                return 0;
            }
            seen.add(num);
        }
        return 1;
    }
}
