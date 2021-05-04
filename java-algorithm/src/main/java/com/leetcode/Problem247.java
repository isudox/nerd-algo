package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Given an integer n, return all the strobogrammatic numbers that
 * are of length n. You may return the answer in any order.
 *
 * A strobogrammatic number is a number that looks the same when
 * rotated 180 degrees (looked at upside down).
 *
 * Example 1:
 *
 * Input: n = 2
 * Output: ["11","69","88","96"]
 * Example 2:
 *
 * Input: n = 1
 * Output: ["0","1","8"]
 *
 * Constraints:
 *
 * 1 <= n <= 14
 */
public class Problem247 {
    public List<String> findStrobogrammatic(int n) {
        List<String> ans = helper(n);
        ans.removeIf(this::isInvalid);
        return ans;
    }
    public List<String> helper(int n) {
        List<String> list1 = new ArrayList<>(Arrays.asList("0", "1", "8"));
        List<String> list2 = new ArrayList<>(Arrays.asList("00", "11", "69", "88", "96"));
        if (n == 1) {
            return list1;
        }
        if (n == 2) {
            return list2;
        }
        List<String> ans = new ArrayList<>();
        int prev = n % 2 == 0 ? n - 2 : n - 1;
        List<String> prevNums = helper(prev);
        int split = prev / 2;
        for (String num : prevNums) {
            for (String interval : (n % 2 == 0 ? list2 : list1)) {
                ans.add(num.substring(0, split) + interval + num.substring(split));
            }
        }
        return ans;
    }

    private boolean isInvalid(String num) {
        return num.length() > 1 && num.startsWith("0");
    }
}
