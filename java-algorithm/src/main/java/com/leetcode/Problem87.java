package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * """87. Scramble String
 * https://leetcode.com/problems/scramble-string/
 *
 * We can scramble a string s to get a string t using the following
 * algorithm:
 *
 * If the length of the string is 1, stop.
 * If the length of the string is > 1, do the following:
 *
 * Split the string into two non-empty substrings at a random index, i.e., if
 * the string is s, divide it to x and y where s = x + y.
 * Randomly decide to swap the two substrings or to keep them in the same order.
 * i.e., after this step, s may become s = x + y or s = y + x.
 * Apply step 1 recursively on each of the two substrings x and y.
 *
 * Given two strings s1 and s2 of the same length, return true if s2 is a
 * scrambled string of s1, otherwise, return false.
 *
 * Example 1:
 *
 * Input: s1 = "great", s2 = "rgeat"
 * Output: true
 * Explanation: One possible scenario applied on s1 is:
 * "great" --> "gr/eat" // divide at random index.
 * "gr/eat" --> "gr/eat" // random decision is not to swap the two substrings
 * and keep them in order.
 * "gr/eat" --> "g/r / e/at" // apply the same algorithm recursively on both
 * substrings. divide at ranom index each of them.
 * "g/r / e/at" --> "r/g / e/at" // random decision was to swap the first
 * substring and to keep the second substring in the same order.
 * "r/g / e/at" --> "r/g / e/ a/t" // again apply the algorithm recursively,
 * divide "at" to "a/t".
 * "r/g / e/ a/t" --> "r/g / e/ a/t" // random decision is to keep both
 * substrings in the same order.
 * The algorithm stops now and the result string is "rgeat" which is s2.
 * As there is one possible scenario that led s1 to be scrambled to s2, we
 * return true.
 *
 * Example 2:
 *
 * Input: s1 = "abcde", s2 = "caebd"
 * Output: false
 *
 * Example 3:
 *
 * Input: s1 = "a", s2 = "a"
 * Output: true
 *
 * Constraints:
 *
 * s1.length == s2.length
 * 1 <= s1.length <= 30
 * s1 and s2 consist of lower-case English letters.
 */
public class Problem87 {
    private char[] chars1;
    private char[] chars2;
    private final Map<String, Integer> memo = new HashMap<>();

    public boolean isScramble(String s1, String s2) {
        this.chars1 = s1.toCharArray();
        this.chars2 = s2.toCharArray();
        return helper(0, chars1.length, 0, chars2.length);
    }

    private boolean helper(int start1, int end1,
                           int start2, int end2) {
        int flag = getCache(start1, end1, start2, end2);
        if (flag == 1)
            return true;
        if (flag == -1)
            return false;
        int len = end1 - start1;
        if (len == 0) {
            setCache(start1, end1, start2, end2, 1);
            return true;
        }
        if (len == 1) {
            if (chars1[start1] == chars2[start2]) {
                setCache(start1, end1, start2, end2, 1);
                return true;
            } else {
                setCache(start1, end1, start2, end2, -1);
                return false;
            }
        }
        if (hasDiff(start1, end1, start2)) {
            setCache(start1, end1, start2, end2, -1);
            return false;
        }
        for (int i = 1, n = end1 - start1; i < n; i++) {
            if ((helper(start1, start1 + i, start2, start2 + i)
                    && helper(start1 + i, end1, start2 + i, end2))
                    || (helper(start1, start1 + i, end2 - i, end2)
                    && helper(start1 + i, end1, start2, end2 - i))) {
                setCache(start1, end1, start2, end2, 1);
                return true;
            }
        }
        setCache(start1, end1, start2, end2, -1);
        return false;
    }

    private boolean hasDiff(int start1, int end1, int start2) {
        int[] counter = new int[26];
        for (int i = 0, n = end1 - start1; i < n; i++) {
            counter[chars1[start1 + i] - 'a']++;
            counter[chars2[start2 + i] - 'a']--;
        }
        for (int v : counter) {
            if (v != 0)
                return true;
        }
        return false;
    }

    private void setCache(int start1, int end1,
                          int start2, int end2,
                          int flag) {
        String key = String.format("%d-%d-%d-%d", start1, end1, start2, end2);
        this.memo.put(key, flag);
    }

    private int getCache(int start1, int end1,
                             int start2, int end2) {
        String key = String.format("%d-%d-%d-%d", start1, end1, start2, end2);
        return this.memo.getOrDefault(key, 0);
    }
}
