package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 1647. Minimum Deletions to Make Character Frequencies Unique
 * https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
 */
public class Problem1647 {
    public int minDeletions(String s) {
        int[] counter = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counter[s.charAt(i) - 'a'] += 1;
        }
        int ans = 0;
        Set<Integer> seen = new HashSet<>();
        for (int i = 0; i < 26; i++) {
            while (counter[i] > 0 && seen.contains(counter[i])) {
                counter[i] -= 1;
                ans += 1;
            }
            seen.add(counter[i]);
        }
        return ans;
    }
}
