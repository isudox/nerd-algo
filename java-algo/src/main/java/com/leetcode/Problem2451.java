package com.leetcode;

import java.util.*;

/**
 * 2451. Odd String Difference
 * https://leetcode.com/problems/odd-string-difference
 */
public class Problem2451 {
    public String oddString(String[] words) {
        Map<String, List<Integer>> store = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            String s = helper(words[i]);
            List<Integer> list = store.getOrDefault(s, new ArrayList<>());
            list.add(i);
            store.put(s, list);
        }
        for (Map.Entry<String, List<Integer>> entry : store.entrySet()) {
            if (entry.getValue().size() == 1) {
                return words[entry.getValue().get(0)];
            }
        }
        return "";
    }

    private String helper(String word) {
        int[] arr = new int[word.length() - 1];
        for (int i = 1; i < word.length(); i++) {
            arr[i - 1] = word.charAt(i) - word.charAt(i - 1);
        }
        return Arrays.toString(arr);
    }
}
