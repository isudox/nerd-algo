package com.leetcode;

import java.util.*;

/**
 * https://leetcode.com/problems/repeated-dna-sequences
 */
public class Problem187 {
    public List<String> findRepeatedDnaSequences(String s) {
        List<String> ans = new ArrayList<>();
        int n = s.length();
        if (n <= 10) {
            return ans;
        }
        Map<String, Integer> seen = new HashMap<>();
        for (int i = 0; i < n - 9; i++) {
            String cur = s.substring(i, i + 10);
            if (!seen.containsKey(cur)) {
                seen.put(cur, 1);
            } else if (seen.get(cur) == 1) {
                ans.add(cur);
                seen.put(cur, 2);
            }
        }
        return ans;
    }
}
