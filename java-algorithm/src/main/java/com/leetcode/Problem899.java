package com.leetcode;

import java.util.Arrays;

/**
 * 899. Orderly Queue
 * https://leetcode.com/problems/orderly-queue/
 */
public class Problem899 {
    public String orderlyQueue(String s, int k) {
        if (k > 1) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            StringBuilder sb = new StringBuilder();
            for (char c : chars) sb.append(c);
            return sb.toString();
        }
        String ans = s;
        for (int i = 0; i < s.length(); i++) {
            String tmp = s.substring(i) + s.substring(0, i);
            if (tmp.compareTo(ans) < 0) {
                ans = tmp;
            }
        }
        return ans;
    }
}
