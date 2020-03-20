package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 22. Generate Parentheses
 * https://leetcode.com/problems/generate-parentheses/
 *
 * Given n pairs of parentheses, write a function to generate all combinations
 * of well-formed parentheses.
 *
 * For example, given n = 3, a solution set is:
 *
 * [
 *   "((()))",
 *   "(()())",
 *   "(())()",
 *   "()(())",
 *   "()()()"
 * ]
 */
public class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        List<String> list = new ArrayList<>();
        if (n <= 0) return list;
        recursive(list, "", n, n);
        return list;
    }
    private void recursive(List<String> result, String paren, int left, int right) {
        if (left == 0 && right == 0) {
            result.add(paren);
            return;
        }
        if (left > 0) {
            recursive(result, paren + "(", left - 1, right);
        }
        if (right > 0 && left < right) {
            recursive(result, paren + ")", left, right - 1);
        }
    }
}
