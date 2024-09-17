package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 884. Uncommon Words from Two Sentences
 * https://leetcode.com/problems/uncommon-words-from-two-sentences/
 */
public class Problem884 {
    public String[] uncommonFromSentences(String s1, String s2) {
        String[] words1 = s1.split(" "), words2 = s2.split(" ");
        Map<String, Integer> counter1 = count(words1), counter2 = count(words2);
        List<String> store = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : counter1.entrySet()) {
            if (entry.getValue() == 1 && !counter2.containsKey(entry.getKey())) {
                store.add(entry.getKey());
            }
        }
        for (Map.Entry<String, Integer> entry : counter2.entrySet()) {
            if (entry.getValue() == 1 && !counter1.containsKey(entry.getKey())) {
                store.add(entry.getKey());
            }
        }
        String[] ans = new String[store.size()];
        for (int i = 0; i < store.size(); i++) {
            ans[i] = store.get(i);
        }
        return ans;
    }

    private Map<String, Integer> count(String[] words) {
        Map<String, Integer> counter = new HashMap<>();
        for (String word : words) {
            counter.put(word, counter.getOrDefault(word, 0) + 1);
        }
        return counter;
    }
}
