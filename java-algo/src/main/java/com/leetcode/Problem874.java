package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 874. Walking Robot Simulation
 * https://leetcode.com/problems/walking-robot-simulation/
 */
public class Problem874 {
    private static final int HASH_MULTIPLIER = 60013; // Slightly larger than 2 * max coordinate value

    public int robotSim(int[] commands, int[][] obstacles) {
        // Store obstacles in an HashSet for efficient lookup
        Set<Integer> obstacleSet = new HashSet<>();
        for (int[] obstacle : obstacles) {
            obstacleSet.add(hashCoordinates(obstacle[0], obstacle[1]));
        }
        // Define direction vectors: North, East, South, West
        int[][] dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        int[] pos = {0, 0};
        int ans = 0;
        int i = 0; // 0: North, 1: East, 2: South, 3: West
        for (int command : commands) {
            if (command == -1) {
                i = (i + 1) % 4;
                continue;
            }
            if (command == -2) {
                i = (i + 3) % 4;
                continue;
            }
            int[] direction = dirs[i];
            for (int step = 0; step < command; step++) {
                int nextX = pos[0] + direction[0];
                int nextY = pos[1] + direction[1];
                if (obstacleSet.contains(hashCoordinates(nextX, nextY))) {
                    break;
                }
                pos[0] = nextX;
                pos[1] = nextY;
            }
            ans = Math.max(ans, pos[0] * pos[0] + pos[1] * pos[1]);
        }
        return ans;
    }

    // Hash function to convert (x, y) coordinates to a unique integer value
    private int hashCoordinates(int x, int y) {
        return x + HASH_MULTIPLIER * y;
    }
}
