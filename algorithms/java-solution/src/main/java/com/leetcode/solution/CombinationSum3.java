package com.leetcode.solution;

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
 * Example 1:
 *
 * Input: k = 3, n = 7
 * Output: [[1,2,4]]
 * Example 2:
 *
 * Input: k = 3, n = 9
 * Output: [[1,2,6], [1,3,5], [2,3,4]]
 */
public class CombinationSum3 {

    public List<List<Integer>> combinationSum3(int k, int n) {
        int[] candidates = new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9};
        List<List<Integer>> ans = new ArrayList<>();
        backtrack(candidates, k, n, 0, new ArrayList<>(), ans);
        return ans;
    }

    private void backtrack(int[] candidates,
                           int k,
                           int target,
                           int start,
                           List<Integer> list,
                           List<List<Integer>> ans) {
        for (int i = start; i < 9; i++) {
            int num = candidates[i];
            if (target < num) {
                break;
            }
            if (list.size() == k - 1) {
                if (target < 10) {
                    list.add(target);
                    ans.add(new ArrayList<>(list));
                    list.remove(list.size() - 1);
                }
                break;
            }
            list.add(num);
            backtrack(candidates, k, target - num, i + 1, list, ans);
            list.remove(list.size() - 1);
        }
    }
}
