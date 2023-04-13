package com.leetcode;

/**
 * 622. Design Circular Queue
 * https://leetcode.com/problems/design-circular-queue/
 */
public class Problem622 {
    private static class MyCircularQueue {
        int[] queue;
        int head;
        int tail;
        int size;

        public MyCircularQueue(int k) {
            queue = new int[k];
            head = 0;
            tail = -1;
            size = 0;
        }

        public boolean enQueue(int value) {
            if (isFull()) return false;
            tail = (tail + 1) % queue.length;
            queue[tail] = value;
            size++;
            return true;
        }

        public boolean deQueue() {
            if (isEmpty()) return false;
            head = (head + 1) % queue.length;
            size--;
            return true;
        }

        public int Front() {
            if (isEmpty()) return -1;
            return queue[head];
        }

        public int Rear() {
            if (isEmpty()) return -1;
            return queue[tail];
        }

        public boolean isEmpty() {
            return size == 0;
        }

        public boolean isFull() {
            return size == queue.length;
        }
    }
}
