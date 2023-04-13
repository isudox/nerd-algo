package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1823. Find the Winner of the Circular Game
 * https://leetcode.com/problems/find-the-winner-of-the-circular-game/
 */
public class Problem1823 {
    public int findTheWinner(int n, int k) {
        List<Integer> players = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            players.add(i);
        }
        int cur = 0;
        while (players.size() > 1) {
            int x = (k + cur) % players.size();
            if (x == 0) {
                x = players.size();
            }
            players.remove(x - 1);
            cur = x - 1 < players.size() ? x - 1 : 0;
        }
        return players.get(0);
    }
}
