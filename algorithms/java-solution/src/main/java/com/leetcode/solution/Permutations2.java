package com.leetcode.solution;

import java.util.ArrayList;
import java.util.List;

/**
 * 47. Permutations II
 * https://leetcode.com/problems/permutations-ii/
 *
 * Given a collection of numbers that might contain duplicates,
 * return all possible unique permutations.
 *
 * Example:
 *
 * Input: [1,1,2]
 * Output:
 * [
 *   [1,1,2],
 *   [1,2,1],
 *   [2,1,1]
 * ]
 */
public class Permutations2 {

    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> permutations = new ArrayList<>();
        int len = nums.length;
        if (len == 0) {
            permutations.add(new ArrayList<>());
            return permutations;
        }
        return permutations;
    }
}
