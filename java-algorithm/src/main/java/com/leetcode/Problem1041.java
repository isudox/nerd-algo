package com.leetcode;

/**
 * https://leetcode.com/problems/robot-bounded-in-circle/
 */
public class Problem1041 {
    public boolean isRobotBounded(String instructions) {
        int[][] dirs = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int d = 0;
        int x = 0, y = 0;
        for (int i = 0; i < instructions.length(); i++) {
            char inst = instructions.charAt(i);
            if (inst == 'G') { // forward
                x += dirs[d][0];
                y += dirs[d][1];
            } else if (inst == 'L') { // turn left
                d = (d + 3) % 4;
            } else {
                d = (d + 1) % 4;
            }
        }
        return (x == 0 && y == 0) || d != 0;
    }
}
