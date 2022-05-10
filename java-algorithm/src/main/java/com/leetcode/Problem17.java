package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 17. Letter Combinations of a Phone Number
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 * <p>
 * Given a string containing digits from 2-9 inclusive, return all possible
 * letter combinations that the number could represent.
 * <p>
 * A mapping of digit to letters (just like on the telephone buttons) is given
 * below. Note that 1 does not map to any letters.
 *
 * <img src="http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png">
 * <p>
 * Example:
 * <p>
 * Input: "23"
 * Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 * Note:
 * <p>
 * Although the above answer is in lexicographical order, your answer could be
 * in any order you want.
 */
public class Problem17 {

    private static final String[] KEY_MAP = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if (digits == null || digits.length() == 0) return res;
        this.combineLetters(digits, "", digits.length(), 0, res);
        return res;
    }

    private void combineLetters(String digits, String str, int len, int pos, List<String> list) {
        String key = KEY_MAP[digits.charAt(pos) - '2'];
        for (int i = 0; i < key.length(); i++) {
            if (pos == len - 1) list.add(str + key.charAt(i));
            else combineLetters(digits, str + key.charAt(i), len, pos + 1, list);
        }
    }

    public List<String> letterCombinations2(String digits) {
        List<String> ans = new ArrayList<>();
        if (digits.length() == 0) {
            return ans;
        }
        dfs("", digits, 0, ans);
        return ans;
    }

    private void dfs(String pre, String digits, int i, List<String> store) {
        if (i == digits.length()) {
            store.add(pre);
            return;
        }
        int pos = digits.charAt(i) - '2';
        for (char next : KEY_MAP[pos].toCharArray()) {
            dfs(pre + next, digits, i + 1, store);
        }
    }
}
