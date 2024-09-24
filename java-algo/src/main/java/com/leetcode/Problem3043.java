package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 3043. Find the Length of the Longest Common Prefix
 * https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
 */
public class Problem3043 {
    public int longestCommonPrefix(int[] arr1, int[] arr2) {
        Set<String> prefix = new HashSet<>();
        for (int num : arr1) {
            String s = "" + num;
            StringBuilder p = new StringBuilder();
            for (int i = 0; i < s.length(); i++) {
                p.append(s.charAt(i));
                prefix.add(p.toString());
            }
        }
        int ans = 0;
        for (int num : arr2) {
            String s = "" + num;
            StringBuilder p = new StringBuilder();
            for (int i = 0; i < s.length(); i++) {
                p.append(s.charAt(i));
                if (!prefix.contains(p.toString())) {
                    break;
                }
                ans = Math.max(ans, i + 1);
            }
        }
        return ans;
    }
}
