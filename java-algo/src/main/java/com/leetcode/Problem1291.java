package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1291. Sequential Digits
 * https://leetcode.com/problems/sequential-digits/
 */
public class Problem1291 {
    public List<Integer> sequentialDigits(int low, int high) {
        List<Integer> ans = new ArrayList<>();
        int len0 = String.valueOf(low).length(), len1 = String.valueOf(high).length();
        for (int i = len0; i <= len1; i++) {
            for (int j = 1; j <= 10 - i; j++) {
                int num = 0;
                for (int k = 0; k < i; k++) {
                    num = num * 10 + j + k;
                }
                if (num >= low && num <= high) {
                    ans.add(num);
                }
            }
        }
        return ans;
    }
}
