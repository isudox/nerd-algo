package com.leetcode;

import java.util.*;

/**
 * 2751. Robot Collisions
 * https://leetcode.com/problems/robot-collisions/
 */
public class Problem2751 {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        Integer[] positionsArray = new Integer[positions.length];
        for (int i = 0; i < positions.length; i++) {
            positionsArray[i] = i;
        }
        Arrays.sort(positionsArray, Comparator.comparingInt(i -> positions[i]));
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i : positionsArray) {
            if (directions.charAt(i) == 'R') {
                q.push(i);
                continue;
            }
            while (!q.isEmpty()) {
                int left = q.peek();
                if (healths[left] < healths[i]) {
                    healths[q.pop()] = 0;
                    healths[i]--;
                } else if (healths[left] > healths[i]) {
                    healths[left]--;
                    healths[i] = 0;
                    break;
                } else {
                    healths[q.pop()] = 0;
                    healths[i] = 0;
                    break;
                }
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int h : healths) {
            if (h > 0) {
                ans.add(h);
            }
        }
        return ans;
    }
}
