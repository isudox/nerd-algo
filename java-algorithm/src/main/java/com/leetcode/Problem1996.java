package com.leetcode;

import java.util.Arrays;

/**
 * 1996. The Number of Weak Characters in the Game
 * https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
 */
public class Problem1996 {
    public int numberOfWeakCharacters(int[][] properties) {
        Arrays.sort(properties, (a, b) -> a[0] == b[0] ? a[1] - b[1] : b[0] - a[0]);
        int ans = 0;
        int maxDefence = 0;
        for (int[] p : properties) {
            if (p[1] < maxDefence) ans++;
            else maxDefence = p[1];
        }
        return ans;
    }
}
