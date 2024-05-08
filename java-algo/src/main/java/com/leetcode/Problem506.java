package com.leetcode;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

/**
 * 506. Relative Ranks
 * https://leetcode.com/problems/relative-ranks/
 */
public class Problem506 {
    public String[] findRelativeRanks(int[] score) {
        int[] sortedScore = Arrays.copyOf(score, score.length);
        Arrays.sort(sortedScore);
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < sortedScore.length; i++) {
            map.put(sortedScore[i], score.length - 1 - i);
        }
        String[] ans = new String[score.length];
        for (int i = 0; i < score.length; i++) {
            int idx = map.get(score[i]);
            switch (idx) {
                case 0 -> ans[i] = "Gold Medal";
                case 1 -> ans[i] = "Silver Medal";
                case 2 -> ans[i] = "Bronze Medal";
                default -> ans[i] = "" + (idx + 1);
            }
        }
        return ans;
    }
}
