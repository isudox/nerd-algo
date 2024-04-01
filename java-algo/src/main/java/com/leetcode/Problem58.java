package com.leetcode;

/**
 * 58. Length of Last Word
 * https://leetcode.com/problems/length-of-last-word/
 */
public class Problem58 {
    public int lengthOfLastWord(String s) {
        String[] ss = s.split(" ");
        for (int i = ss.length - 1; i >= 0; i--) {
            if (!ss[i].isEmpty()) {
                return ss[i].length();
            }
        }
        return 0;
    }
}
