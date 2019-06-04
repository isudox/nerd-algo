package com.leetcode;

/**
 * 28. Implement strStr()
 * https://leetcode.com/problems/implement-strstr/
 *
 * Return the index of the first occurrence of needle in haystack,
 * or -1 if needle is not part of haystack.
 *
 * Example 1:
 *
 * Input: haystack = "hello", needle = "ll"
 * Output: 2
 *
 * Example 2:
 *
 * Input: haystack = "aaaaa", needle = "bba"
 * Output: -1
 * Clarification:
 *
 * What should we return when needle is an empty string?
 * This is a great question to ask during an interview.
 *
 * For the purpose of this problem, we will return 0 when needle is an empty
 * string. This is consistent to C's strstr() and Java's indexOf().
 */
public class ImplementStrStr {

    public int strStr(String haystack, String needle) {
        if (needle.equals(""))
            return 0;
        if (haystack.length() < needle.length())
            return -1;
        int i = 0, j = 0, start = 0;
        while (i < haystack.length() && j < needle.length()) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
            } else {
                i = i - j + 1;
                j = 0;
            }
            if (j == needle.length())
                return i - j;
        }
        return -1;
    }
}
