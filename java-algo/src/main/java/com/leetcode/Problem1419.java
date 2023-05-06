package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 1419. Minimum Number of Frogs Croaking
 * https://leetcode.com/problems/minimum-number-of-frogs-croaking/
 */
public class Problem1419 {
    public int minNumberOfFrogs(String croakOfFrogs) {
        int n = croakOfFrogs.length();
        if (n % 5 != 0 || croakOfFrogs.charAt(0) != 'c' || croakOfFrogs.charAt(n - 1) != 'k') {
            return -1;
        }
        Map<Character, Integer> dict = new HashMap<>();
        dict.put('c', 0);
        dict.put('r', 1);
        dict.put('o', 2);
        dict.put('a', 3);
        dict.put('k', 4);
        int ans = 0;
        int[] counter = new int[5];
        for (int i = 0; i < n; i++) {
            char c = croakOfFrogs.charAt(i);
            int x = dict.get(c);
            if (x == 0 && counter[x] == 0) {
                ans++;
                counter[x] += 1;
            } else if (counter[x] < 1) {
                return -1;
            }
            counter[x] -= 1;
            counter[(x + 1) % 5] += 1;
        }
        return counter[0] == ans ? ans : -1;
    }
}
