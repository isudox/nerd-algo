package com.leetcode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * 2032. Two Out of Three
 * https://leetcode.com/problems/two-out-of-three/
 */
public class Problem2032 {
    public List<Integer> twoOutOfThree(int[] nums1, int[] nums2, int[] nums3) {
        int[] counter = new int[101];
        Set<Integer> seen = new HashSet<>();
        count(nums1, counter, seen);
        count(nums2, counter, seen);
        count(nums3, counter, seen);
        List<Integer> ans = new ArrayList<>();
        for (int i = 1; i <= 100; i++) {
            if (counter[i] >= 2) {
                ans.add(i);
            }
        }
        return ans;
    }

    private void count(int[] nums, int[] counter, Set<Integer> seen) {
        for (int num : nums) {
            if (!seen.contains(num)) {
                seen.add(num);
                counter[num]++;
            }
        }
        seen.clear();
    }
}
