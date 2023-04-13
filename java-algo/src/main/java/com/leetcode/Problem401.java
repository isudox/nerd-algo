package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class Problem401 {

    private static final int[] TIMES = {8, 4, 2, 1, 32, 16, 8, 4, 2, 1};

    public List<String> readBinaryWatch(int turnedOn) {
        int[] leds = new int[10];
        List<String> ans = new ArrayList<>();
        backtrack(0, turnedOn, leds, ans);
        return ans;
    }

    private void backtrack(int i, int rem, int[] leds, List<String> ans) {
        if (rem == 0) {
            String time = getTime(leds);
            if (!time.equals("")) {
                ans.add(getTime(leds));
            }
            return;
        }
        if (i == 10)
            return;
        leds[i] = 1;
        backtrack(i + 1, rem - 1, leds, ans);
        leds[i] = 0;
        backtrack(i + 1, rem, leds, ans);
    }

    private String getTime(int[] leds) {
        int h = 0, m = 0;
        for (int i = 0; i < 4; i++) {
            if (leds[i] == 1)
                h += TIMES[i];
            if (h > 11) {
                return "";
            }
        }
        for (int j = 4; j < 10; j++) {
            if (leds[j] == 1)
                m += TIMES[j];
            if (m > 59) {
                return "";
            }
        }
        return String.format("%d:%02d", h, m);
    }

    public List<String> readBinaryWatch2(int turnedOn) {
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < 60; j++) {
                if (Integer.bitCount(i) + Integer.bitCount(j) == turnedOn) {
                    ans.add(String.format("%d:%02d", i, j));
                }
            }
        }
        return ans;
    }

    public List<String> readBinaryWatch3(int turnedOn) {
        List<String> ans = new ArrayList<>();
        for (int i = 0; i < 1024; i++) {
            int h = i >> 6;
            int m = i & 0b111111;
            if (h < 12 && m < 60 && Integer.bitCount(i) == turnedOn) {
                ans.add(String.format("%d:%02d", h, m));
            }
        }
        return ans;
    }

}
