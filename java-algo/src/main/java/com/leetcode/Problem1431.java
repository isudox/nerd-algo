package com.leetcode;

import java.util.ArrayList;
import java.util.List;

public class Problem1431 {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = candies[0];
        for (int candy : candies) {
            if (candy > max) {
                max = candy;
            }
        }
        List<Boolean> ans = new ArrayList<>();
        for (int candy : candies) {
            ans.add(candy + extraCandies >= max);
        }
        return ans;
    }
}
