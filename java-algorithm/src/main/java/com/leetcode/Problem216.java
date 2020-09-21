package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 216. Combination Sum III
 * https://leetcode.com/problems/combination-sum-iii/
 *
 * Find all possible combinations of k numbers that add up to a number n,
 * given that only numbers from 1 to 9 can be used and each combination
 * should be a unique set of numbers.
 *
 * Note:
 *
 * All numbers will be positive integers.
 * The solution set must not contain duplicate combinations.
 *
 * Example 1:
 *
 * Input: k = 3, n = 7
 * Output: [[1,2,4]]
 *
 * Example 2:
 *
 * Input: k = 3, n = 9
 * Output: [[1,2,6], [1,3,5], [2,3,4]]
 */
public class Problem216 {

    public List<List<Integer>> combinationSum3(int k, int n) {
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(k, n, 1, new ArrayList<>(), ans);
        return ans;
    }

    private void backtrack(int k,
                           int target,
                           int start,
                           List<Integer> candidate,
                           List<List<Integer>> ans) {
        for (int i = start; i <= 9; i++) {
            if (target < i)
                break;
            if (candidate.size() == k - 1) {
                if (target < 10) {
                    candidate.add(target);
                    ans.add(new ArrayList<>(candidate));
                    candidate.remove(candidate.size() - 1);
                }
                break;
            }
            candidate.add(i);
            backtrack(k, target - i, i + 1, candidate, ans);
            candidate.remove(candidate.size() - 1);
        }
    }
}
