package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Problem1262 {
    public int maxSumDivThree(int[] nums) {
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % 3 == 0) {
            return sum;
        }
        Arrays.sort(nums);
        List<Integer>[] groups = new List[3];
        for (int i = 0; i < 3; i++) {
            groups[i] = new ArrayList<>();
        }
        for (int num : nums) {
            List<Integer> list = groups[num % 3];
            if (list.size() >= 3) {
                continue;
            }
            list.add(num);
            groups[num % 3] = list;
        }
        int d = sum % 3;
        int del = sum;
        if (groups[d].size() > 0) {
            del = Math.min(del, groups[d].get(0));
        }
        if (groups[(3 - d) % 3].size() >= 2) {
            del = Math.min(del, groups[(3 - d) % 3].get(0) + groups[(3 - d) % 3].get(1));
        }
        return sum - del;
    }
}
