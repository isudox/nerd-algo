package com.leetcode;

import java.util.HashMap;
import java.util.Map;

/**
 * 2024. Maximize the Confusion of an Exam
 * https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
 */
public class Problem2024 {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        int ans = 0;
        Map<Character, Integer> count = new HashMap<>();
        for (int i = 0; i < answerKey.length(); i++) {
            char c = answerKey.charAt(i);
            count.put(c, count.getOrDefault(c, 0) + 1);
            int min = Math.min(count.getOrDefault('T', 0), count.getOrDefault('F', 0));
            if (min <= k) {
                ans++;
            } else {
                char d = answerKey.charAt(i - ans);
                count.put(d, count.get(d) - 1);
            }
        }
        return ans;
    }
}
