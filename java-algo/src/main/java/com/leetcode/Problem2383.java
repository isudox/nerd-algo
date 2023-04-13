package com.leetcode;

/**
 * 2383. Minimum Hours of Training to Win a Competition
 * https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/
 */
public class Problem2383 {
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int sum = 0;
        for (int e : energy) {
            sum += e;
        }
        int ans = initialEnergy > sum ? 0 : sum + 1 - initialEnergy;
        for (int e : experience) {
            if (initialEnergy <= e) {
                ans += 1 + e - initialEnergy;
                initialExperience = 2 * e + 1;
            } else {
                initialExperience += e;
            }
        }
        return ans;
    }
}
