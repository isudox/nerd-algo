package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 2405. Optimal Partition of String
 * https://leetcode.com/problems/optimal-partition-of-string/
 */
public class Problem2405 {
    public int partitionString(String s) {
        Set<Character> seen = new HashSet<>();
        int ans = 1;
        int i = 0;
        while (i < s.length()) {
            if (seen.contains(s.charAt(i))) {
                ans++;
                seen.clear();
            }
            seen.add(s.charAt(i++));
        }
        return ans;
    }
}
