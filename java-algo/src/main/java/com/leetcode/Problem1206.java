package com.leetcode;

import java.util.Arrays;
import java.util.Random;

/**
 * 1206. Design Skiplist
 * https://leetcode.com/problems/design-skiplist/
 */
public class Problem1206 {
    private static class Skiplist {
        private static final int MAX_LEVELS = 32;
        private static final double FACTOR = 0.25;
        private Node node;
        private int level;
        private Random random;

        public Skiplist() {
            node = new Node(-1, MAX_LEVELS);
            random = new Random();
        }

        public boolean search(int target) {
            Node cur = node;
            for (int i = level - 1; i >= 0; i--) {
                while (cur.siblings[i] != null && cur.siblings[i].val < target) {
                    cur = cur.siblings[i];
                }
            }
            cur = cur.siblings[0];
            return cur != null && cur.val == target;
        }

        public void add(int num) {
            Node[] update = new Node[MAX_LEVELS];
            Arrays.fill(update, node);
            Node cur = node;
            for (int i = level - 1; i >= 0; i--) {
                while (cur.siblings[i] != null && cur.siblings[i].val < num) {
                    cur = cur.siblings[i];
                }
                update[i] = cur;
            }
            int newLevel = getRandomLevel();
            this.level = Math.max(this.level, newLevel);
            Node newNode = new Node(num, level);
            for (int i = 0; i < newLevel; i++) {
                newNode.siblings[i] = update[i].siblings[i];
                update[i].siblings[i] = newNode;
            }
        }

        public boolean erase(int num) {
            Node[] update = new Node[MAX_LEVELS];
            Node cur = this.node;
            for (int i = level - 1; i >= 0; i--) {
                while (cur.siblings[i] != null && cur.siblings[i].val < num) {
                    cur = cur.siblings[i];
                }
                update[i] = cur;
            }
            cur = cur.siblings[0];
            if (cur == null || cur.val != num) return false;
            for (int i = 0; i < level; i++) {
                if (update[i].siblings[i] != cur) break;
                update[i].siblings[i] = cur.siblings[i];
            }
            while (level > 1 && node.siblings[level - 1] == null) {
                level--;
            }
            return true;
        }

        private int getRandomLevel() {
            int level = 1;
            while (random.nextDouble() < FACTOR && level < MAX_LEVELS) {
                level++;
            }
            return level;
        }
    }

    private static class Node {
        int val;
        Node[] siblings;

        public Node(int val, int levels) {
            this.val = val;
            this.siblings = new Node[levels];
        }
    }
}


