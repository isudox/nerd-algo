package com.leetcode;

import java.util.HashSet;
import java.util.Set;

public class Problem2744 {
    public int maximumNumberOfStringPairs(String[] words) {
        int ans = 0;
        Set<String> seen = new HashSet<>();
        for (String word : words) {
            String rev = reverse(word);
            if (seen.contains(rev)) {
                ans++;
            }
            seen.add(word);
        }
        return ans;
    }

    private String reverse(String word) {
        StringBuilder sb = new StringBuilder();
        for (int i = word.length() - 1; i >= 0; i--) {
            sb.append(word.charAt(i));
        }
        return sb.toString();
    }
}
