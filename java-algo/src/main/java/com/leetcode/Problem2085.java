package com.leetcode;

import java.util.HashMap;
import java.util.Map;

public class Problem2085 {
    public int countWords(String[] words1, String[] words2) {
        Map<String, Integer> counts1 = count(words1), counts2 = count(words2);
        int ans = 0;
        for (Map.Entry<String, Integer> entry : counts1.entrySet()) {
            if (entry.getValue() == 1 && counts2.getOrDefault(entry.getKey(), 0) == 1) {
                ans++;
            }
        }
        return ans;
    }

    private Map<String, Integer> count(String[] words) {
        Map<String, Integer> counts = new HashMap<>();
        for (String word : words) {
            counts.put(word, counts.getOrDefault(word, 0) + 1);
        }
        return counts;
    }
}
