package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1404. Number of Steps to Reduce a Number in Binary Representation to One
 * https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
 */
public class Problem1404 {
    public int numSteps(String s) {
        List<Integer> nums = new ArrayList<>();
        for (char c : s.toCharArray()) {
            nums.add(c - '0');
        }
        int ans = 0;
        while (nums.size() > 1) {
            ans++;
            if (nums.get(nums.size() - 1) == 0) {
                nums.remove(nums.size() - 1);
                continue;
            }
            int pre = 1;
            for (int i = nums.size() - 1; i >= 0; i--) {
                int cur = nums.get(i) + pre;
                pre = cur / 2;
                cur = cur % 2;
                nums.set(i, cur);
                if (pre == 0) {
                    break;
                }
            }
            if (pre == 1) {
                nums.add(0, 1);
            }
        }
        return ans;
    }
}
