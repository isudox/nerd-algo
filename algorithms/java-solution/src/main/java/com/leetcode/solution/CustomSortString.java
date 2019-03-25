package com.leetcode.solution;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 791. Custom Sort String
 * https://leetcode.com/problems/custom-sort-string/
 *
 * `S` and `T` are strings composed of lowercase letters. In `S`,
 * no letter occurs more than once.
 *
 * S was sorted in some custom order previously. We want to permute the characters
 * of T so that they match the order that S was sorted. More specifically,
 * if x occurs before y in S, then x should occur before y in the returned string.
 *
 * Return any permutation of T (as a string) that satisfies this property.
 *
 * Example 1:
 *
 * Input:
 * S = "cba"
 * T = "abcd"
 * Output: "cbad"
 * Explanation:
 * "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
 * Since "d" does not appear in S, it can be at any position in T.
 * "dcba", "cdba", "cbda" are also valid outputs.
 *
 * Example 2:
 *
 * Input:
 * S = "kqep"
 * T = "pekeq"
 * Output: "kqeep"
 *
 *
 * Note:
 *
 * S has length at most 26, and no character is repeated in S.
 * T has length at most 200.
 * S and T consist of lowercase letters only.
 */
public class CustomSortString {

    public String customSortString(String s, String t) {
        Map<Character, Integer> map = new HashMap<>();
        List<Integer> list = new ArrayList<>();
        int tLen = t.length(), sLen = s.length();

        for (int i = 0; i < tLen; i++) {
            char c = t.charAt(i);
            if (s.contains(Character.toString(c))) {
                list.add(i);
                map.put(c, map.getOrDefault(c, 0) + 1);
            }
        }
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < sLen; i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                for (int j = 0; j < map.get(c); j++) {
                    ans.append(c);
                }
            }
        }
        for (int i = 0; i < tLen; i++) {
            if (!list.contains(i)) {
                ans.append(t.charAt(i));
            }
        }

        return ans.toString();
    }
}
