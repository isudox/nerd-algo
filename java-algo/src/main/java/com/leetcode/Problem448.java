package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class Problem448 {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int[] counter = new int[nums.length + 1];
        for (int num : nums) {
            counter[num]++;
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = 1; i <= nums.length; i++) {
            if (counter[i] == 0) {
                ans.add(i);
            }
        }
        return ans;
    }
}
