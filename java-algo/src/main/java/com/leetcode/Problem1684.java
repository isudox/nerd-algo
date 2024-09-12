package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 1684. Count the Number of Consistent Strings
 * https://leetcode.com/problems/count-the-number-of-consistent-strings
 */
public class Problem1684 {
    public int countConsistentStrings(String allowed, String[] words) {
        int cnt = 0;
        Set<Character> set = new HashSet<>();
        for (char c : allowed.toCharArray()) {
            set.add(c);
        }
        for (String word : words) {
            for (char c : word.toCharArray()) {
                if (!set.contains(c)) {
                    cnt++;
                    break;
                }
            }
        }
        return words.length - cnt;
    }
}
