package com.leetcode;

import java.util.*;

/**
 * 950. Reveal Cards In Increasing Order
 * https://leetcode.com/problems/reveal-cards-in-increasing-order
 */
public class Problem950 {
    public int[] deckRevealedIncreasing(int[] deck) {
        Deque<Integer> q = new ArrayDeque<>();
        for (int num : deck) {
            q.offerLast(num);
        }
        Map<Integer, Integer> map = new HashMap<>();
        int idx = 0;
        while (!q.isEmpty()) {
            map.put(q.pollFirst(), idx++);
            if (!q.isEmpty()) {
                q.offerLast(q.pollFirst());
            }
        }
        int[] ans = new int[deck.length], temp = deck.clone();
        Arrays.sort(temp);
        for (int i = 0; i < deck.length; i++) {
            ans[i] = temp[map.get(deck[i])];
        }
        return ans;
    }
}
