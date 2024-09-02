package com.leetcode;

/**
 * 1894. Find the Student that Will Replace the Chalk
 * https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/
 */
public class Problem1894 {
    public int chalkReplacer(int[] chalk, int k) {
        long sum = 0;
        for (int num : chalk) {
            sum += num;
        }
        k %= sum;
        int i = 0;
        while (k >= chalk[i]) {
            k -= chalk[i];
            i = (++i) % chalk.length;
        }
        return i;
    }
}
