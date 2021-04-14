package com.leetcode;

import java.util.Arrays;

class Problem179 {
    public String largestNumber(int[] nums) {
        String[] strings = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strings[i] = String.valueOf(nums[i]);
        }
        Arrays.sort(strings, (o1, o2) -> {
            long x = Long.parseLong(o1 + o2);
            long y = Long.parseLong(o2 + o1);
            return (int) (y - x);
        });
        if ("0".equals(strings[0]))
            return "0";
        return String.join("", strings);
    }
}
