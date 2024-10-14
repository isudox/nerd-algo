package com.leetcode;

import java.util.*;

/**
 * 1942. The Number of the Smallest Unoccupied Chair
 */
public class Problem1942 {
    public int smallestChair(int[][] times, int targetFriend) {
        Map<Integer, Integer> arrives = new HashMap<>();
        Map<Integer, List<Integer>> leaves = new HashMap<>();
        Map<Integer, Integer> occupied = new HashMap<>(); // friend: chair
        for (int i = 0; i < times.length; i++) {
            int arrive = times[i][0], leave = times[i][1];
            arrives.put(arrive, i);
            List<Integer> list = leaves.getOrDefault(leave, new ArrayList<>());
            list.add(i);
            leaves.put(leave, list);
        }
        int chair = 0;
        List<Integer> list = new LinkedList<>();
        for (int t = 1; t <= times[targetFriend][1]; t++) {
            for (int left : leaves.getOrDefault(t, new ArrayList<>())) {
                list.add(occupied.get(left));
                list.sort(Integer::compareTo);
            }
            if (!arrives.containsKey(t)) {
                continue;
            }
            int friend = arrives.get(t);
            if (list.isEmpty()) {
                occupied.put(friend, chair++);
            } else {
                occupied.put(friend, list.remove(0));
            }
        }
        return occupied.get(targetFriend);
    }

    public static void main(String[] args) {
        Problem1942 solution = new Problem1942();
        System.out.println(solution.smallestChair(new int[][]{{1, 4}, {2, 3}, {4, 6}}, 1));
        System.out.println(solution.smallestChair(new int[][]{{3, 10}, {1, 5}, {2, 6}}, 0));
    }
}
