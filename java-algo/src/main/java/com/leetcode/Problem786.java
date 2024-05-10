package com.leetcode;

import java.util.PriorityQueue;

/**
 * 786. K-th Smallest Prime Fraction
 */
public class Problem786 {
    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[1] * b[0] - a[0] * b[1]);
        for (int i = 0; i < arr.length; i++) {
            for (int j = arr.length - 1; j > i; j--) {
                if (heap.size() < k) {
                    heap.add(new int[]{arr[i], arr[j]});
                } else {
                    int[] peek = heap.peek();
                    if (peek[0] * arr[j] > peek[1] * arr[i]) {
                        heap.poll();
                        heap.add(new int[]{arr[i], arr[j]});
                    }
                }
            }
        }
        return heap.peek();
    }
}
