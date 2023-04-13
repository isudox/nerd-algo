package com.leetcode;

import java.util.*;

/**
 * 1239. Maximum Length of a Concatenated String with Unique Characters
 * https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
 */
public class Problem1239 {
    public int maxLength(List<String> arr) {
        Iterator<String> iterator = arr.iterator();
        while (iterator.hasNext()) {
            String word = iterator.next();
            Set<Character> seen = new HashSet<>();
            for (int i = 0; i < word.length(); i++) {
                if (seen.contains(word.charAt(i))) {
                    iterator.remove();
                    break;
                } else {
                    seen.add(word.charAt(i));
                }
            }
        }
        int ans = 0;
        int n = arr.size();
        int limit = 1 << n;
        for (int i = 0; i < limit; i++) {
            int bits = i;
            int pos = n - 1;
            int[] counter = new int[26];
            int len = 0;
            while (bits > 0) {
                if ((bits & 1) == 1) {
                    counter = merge(counter, arr.get(pos));
                    if (counter == null) {
                        break;
                    }
                    len += arr.get(pos).length();
                    ans = Math.max(ans, len);
                }
                bits >>= 1;
                pos--;
            }
        }
        return ans;
    }

    private int[] merge(int[] merged, String word) {
        for (int i = 0; i < word.length(); i++) {
            int pos = word.charAt(i) - 'a';
            if (merged[pos] > 0) {
                return null;
            }
            merged[pos]++;
        }
        return merged;
    }
}
