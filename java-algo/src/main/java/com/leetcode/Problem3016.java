package com.leetcode;

import java.util.*;

/**
 * 3016. Minimum Number of Pushes to Type Word II
 * https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
 */
public class Problem3016 {
    public int minimumPushes(String word) {
        int ans = 0;
        int[] count = new int[26];
        for (int i = 0; i < word.length(); i++) {
            count[word.charAt(i) - 'a']++;
        }
        TreeMap<Integer, List<Integer>> map = new TreeMap<>();
        for (int i = 0; i < 26; i++) {
            if (count[i] > 0) {
                List<Integer> list = map.getOrDefault(count[i], new ArrayList<>());
                list.add(i);
                map.put(count[i], list);
            }
        }
        int[] store = new int[8];
        int index = 0;
        for (int cnt : map.descendingKeySet()) {
            for (int i = 0; i < map.get(cnt).size(); i++) {
                store[index]++;
                ans += cnt * (store[index]);
                if (++index == 8) {
                    index = 0;
                }
            }
        }
        return ans;
    }
}
