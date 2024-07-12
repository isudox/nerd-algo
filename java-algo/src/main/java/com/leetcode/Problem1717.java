package com.leetcode;

import java.util.Stack;

/**
 * 1717. Maximum Score From Removing Substrings
 * https://leetcode.com/problems/maximum-score-from-removing-substrings/
 */
public class Problem1717 {
    public int maximumGain(String s, int x, int y) {
        String hi = x > y ? "ab" : "ba";
        String lo = x > y ? "ba" : "ab";
        int ans = 0;
        String rem0 = helper(s, hi);
        ans += (s.length() - rem0.length()) / 2 * Math.max(x, y);
        String rem1 = helper(rem0, lo);
        ans += (rem0.length() - rem1.length()) / 2 * Math.min(x, y);
        return ans;
    }

    private String helper(String s, String t) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char cur = s.charAt(i);
            if (stack.isEmpty()) {
                stack.push(cur);
                continue;
            }
            if (t.equals("" + stack.peek() + cur)) {
                stack.pop();
            } else {
                stack.push(cur);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (Character character : stack) {
            sb.append(character);
        }
        return sb.toString();
    }
}
