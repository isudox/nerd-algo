package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 17. Letter Combinations of a Phone Number
 * https://leetcode.com/problems/letter-combinations-of-a-phone-number/
 */
public class Problem17 {

    private static final String[] KEYS = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    public List<String> letterCombinations(String digits) {
        List<String> res = new ArrayList<>();
        if (digits == null || digits.length() == 0) {
            return res;
        }
        this.combineLetters(digits, "", digits.length(), 0, res);
        return res;
    }

    private void combineLetters(String digits, String str, int len, int pos, List<String> list) {
        String key = KEYS[digits.charAt(pos) - '2'];
        for (int i = 0; i < key.length(); i++) {
            if (pos == len - 1) {
                list.add(str + key.charAt(i));
            } else {
                combineLetters(digits, str + key.charAt(i), len, pos + 1, list);
            }
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
        for (char next : KEYS[pos].toCharArray()) {
            dfs(pre + next, digits, i + 1, store);
        }
    }

    public List<String> letterCombinations3(String digits) {
        List<String> ans = new ArrayList<>();
        if (digits.length() == 0) {
            return ans;
        }
        ans.add("");
        for (int i = 0; i < digits.length(); i++) {
            int n = ans.size();
            for (int j = 0; j < n; j++) {
                String pre = ans.remove(0);
                for (char ch : KEYS[digits.charAt(i) - '2'].toCharArray()) {
                    ans.add(pre + ch);
                }
            }
        }
        return ans;
    }
}
