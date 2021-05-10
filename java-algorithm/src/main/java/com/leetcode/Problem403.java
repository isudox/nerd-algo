package com.leetcode;

import java.util.HashSet;
import java.util.Set;

/**
 * 403. Frog Jump
 * https://leetcode.com/problems/frog-jump/
 *
 * A frog is crossing a river. The river is divided into some number of units,
 * and at each unit, there may or may not exist a stone. The frog can jump on a
 * stone, but it must not jump into the water.
 *
 * Given a list of stones' positions (in units) in sorted ascending order,
 * determine if the frog can cross the river by landing on the last stone.
 * Initially, the frog is on the first stone and assumes the first jump must be
 * 1 unit.
 *
 * If the frog's last jump was k units, its next jump must be either k - 1, k,
 * or k + 1 units. The frog can only jump in the forward direction.
 *
 * Example 1:
 *
 * Input: stones = [0,1,3,5,6,8,12,17]
 * Output: true
 * Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd
 * stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3
 * units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th
 * stone.
 *
 * Example 2:
 *
 * Input: stones = [0,1,2,3,4,8,9,11]
 * Output: false
 * Explanation: There is no way to jump to the last stone as the gap between the
 * 5th and 6th stone is too large.
 *
 * Constraints:
 *
 * 2 <= stones.length <= 2000
 * 0 <= stones[i] <= 2^31 - 1
 * stones[0] == 0
 */
public class Problem403 {
    /**
     * DFS with memo
     */
    public boolean canCross(int[] stones) {
        int n = stones.length;
        Set<Integer>[] attempts = new HashSet[n];
        for (int i = 0; i < n; i++) {
            attempts[i] = new HashSet<>();
        }
        return dfs(attempts, stones, 0, 0);
    }

    private boolean dfs(Set<Integer>[] attempts, int[] stones, int index, int jump) {
        if (attempts[index].contains(jump)) {
            return false;
        }
        if (index == stones.length - 1) {
            return true;
        }
        for (int nextJump = Math.max(1, jump - 1); nextJump <= jump + 1; nextJump++) {
            int nextStone = stones[index] + nextJump;
            for (int nextIndex = index + 1; nextIndex < stones.length; nextIndex++) {
                if (stones[nextIndex] == nextStone) {
                    if (dfs(attempts, stones, nextIndex, nextJump)) {
                        return true;
                    }
                } else if (stones[nextIndex] > nextStone) {
                    break;
                }
            }
        }
        attempts[index].add(jump);
        return false;
    }

    /**
     * DP
     */
    public boolean canCross2(int[] stones) {
        int n = stones.length;
        for (int i = 1; i < n; i++) {
            if (stones[i] - stones[i - 1] > i) {
                return false;
            }
        }
        boolean[][] dp = new boolean[n][n];
        dp[0][0] = true;
        for (int i = 1; i < n; i++) {
            for (int j = i - 1; j >= 0; j--) {
                int jump = stones[i] - stones[j];
                if (jump > j + 1) {
                    break;
                }
                dp[i][jump] = dp[j][jump - 1] || dp[j][jump] || dp[j][jump + 1];
                if (i == n - 1 && dp[i][jump]) {
                    return true;
                }
            }
        }
        return false;
    }
}
