package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 2149. Rearrange Array Elements by Sign
 * https://leetcode.com/problems/rearrange-array-elements-by-sign/
 */
public class Problem2149 {
    public int[] rearrangeArray(int[] nums) {
        List<Integer>[] groups = new List[2];
        groups[0] = new ArrayList<>();
        groups[1] = new ArrayList<>();
        for (int num : nums) {
            if (num > 0) {
                groups[0].add(num);
            } else {
                groups[1].add(num);
            }
        }
        int[] ans = new int[nums.length];
        int i = 0;
        while (i < nums.length) {
            ans[i] = groups[i % 2].get(i / 2);
            i++;
        }
        return ans;
    }
}
