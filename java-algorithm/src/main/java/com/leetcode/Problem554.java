package com.leetcode;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * 554. Brick Wall
 * https://leetcode.com/problems/brick-wall/
 *
 * There is a rectangular brick wall in front of you with n rows of bricks. The
 * i^th row has some number of bricks each of the same height (i.e., one unit)
 * but they can be of different widths. The total width of each row is the
 * same.
 *
 * Draw a vertical line from the top to the bottom and cross the least bricks.
 * If your line goes through the edge of a brick, then the brick is not
 * considered as crossed. You cannot draw a line just along one of the two
 * vertical edges of the wall, in which case the line will obviously cross no
 * bricks.
 *
 * Given the 2D array wall that contains the information about the wall, return
 * the minimum number of crossed bricks after drawing such a vertical line.
 *
 * Example 1:
 *
 * Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
 * Output: 2
 *
 * Example 2:
 *
 * Input: wall = [[1],[1],[1]]
 * Output: 3
 *
 * Constraints:
 *
 * n == wall.length
 * 1 <= n <= 10^4
 * 1 <= wall[i].length <= 10^4
 * 1 <= sum(wall[i].length) <= 2 * 10^4
 * sum(wall[i]) is the same for each row i.
 * 1 <= wall[i][j] <= 2^31 - 1
 */
public class Problem554 {
    public int leastBricks(List<List<Integer>> wall) {
        int ans = wall.size();
        Map<Integer, Integer> counter = new HashMap<>();
        for (List<Integer> bricks : wall) {
            int segment = 0;
            for (int i = 0; i < bricks.size() - 1; i++) {
                segment += bricks.get(i);
                int count = counter.getOrDefault(segment, wall.size()) - 1;
                counter.put(segment, count);
                if (count < ans) {
                    ans = count;
                }
            }
        }
        return ans;
    }
}
