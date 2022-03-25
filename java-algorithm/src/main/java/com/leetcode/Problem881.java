package com.leetcode;

import java.util.Arrays;

/**
 * 881. Boats to Save People
 * https://leetcode.com/problems/boats-to-save-people/
 */
public class Problem881 {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, j = people.length - 1;
        int ans = 0;
        while (i < j) {
            if (people[i] + people[j] <= limit) i++;
            ans += 1;
            j--;
        }
        if (i == j) {
            ans++;
        }
        return ans;
    }
}
