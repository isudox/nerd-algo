package com.leetcode;

import java.util.List;
import java.util.Objects;

/**
 * 1773. Count Items Matching a Rule
 * https://leetcode.com/problems/count-items-matching-a-rule/
 */
public class Problem1773 {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int ans = 0;
        int id = 0;
        if (Objects.equals(ruleKey, "color")) {
            id = 1;
        }
        if (Objects.equals(ruleKey, "name")) {
            id = 2;
        }
        for (List<String> item : items) {
            if (ruleValue.equals(item.get(id))) {
                ans++;
            }
        }
        return ans;
    }
}
