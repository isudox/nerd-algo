package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 1276. Number of Burgers with No Waste of Ingredients
 * https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/
 */
public class Problem1276 {
    public List<Integer> numOfBurgers(int tomatoSlices, int cheeseSlices) {
        List<Integer> ans = new ArrayList<>();
        int x = (tomatoSlices - cheeseSlices * 2) / 2;
        if (x < 0 || (x * 2) != tomatoSlices - cheeseSlices * 2) {
            return ans;
        }
        int y = cheeseSlices - x;
        if (y < 0) {
            return ans;
        }
        ans.add(x);
        ans.add(y);
        return ans;
    }
}
