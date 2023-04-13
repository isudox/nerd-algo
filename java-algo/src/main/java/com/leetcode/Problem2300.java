package com.leetcode;

import java.util.Arrays;

/**
 * 2300. Successful Pairs of Spells and Potions
 * https://leetcode.com/problems/successful-pairs-of-spells-and-potions/
 */
public class Problem2300 {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int m = spells.length, n = potions.length;
        int[] ans = new int[m];
        Arrays.sort(potions);
        for (int i = 0; i < m; i++) {
            long need = success / spells[i] + (success % spells[i] > 0 ? 1 : 0);
            if (need > potions[n - 1]) {
                ans[i] = 0;
                continue;
            }
            ans[i] = find(potions, (int) need);
        }
        return ans;
    }

    private int find(int[] nums, int num) {
        if (nums[nums.length - 1] < num) {
            return 0;
        }
        if (nums[0] >= num) {
            return nums.length;
        }
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] >= num) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return nums.length - lo;
    }
}
