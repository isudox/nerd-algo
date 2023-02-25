package com.leetcode;

import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;

public class Problem460 {
    static class Pair<T1, T2> {
        T1 first;
        T2 second;

        public Pair(T1 first, T2 second) {
            this.first = first;
            this.second = second;
        }
    }

    static class LFUCache {
        // key: original key, value: frequency and original value.
        private Map<Integer, Pair<Integer, Integer>> cache;
        // key: frequency, value: All keys that have the same frequency.
        private Map<Integer, LinkedHashSet<Integer>> frequencies;
        private int minf;
        private int capacity;

        private void insert(int key, int frequency, int value) {
            cache.put(key, new Pair<>(frequency, value));
            frequencies.putIfAbsent(frequency, new LinkedHashSet<>());
            frequencies.get(frequency).add(key);
        }

        public LFUCache(int capacity) {
            cache = new HashMap<>();
            frequencies = new HashMap<>();
            minf = 0;
            this.capacity = capacity;
        }

        public int get(int key) {
            Pair<Integer, Integer> frequencyAndValue = cache.get(key);
            if (frequencyAndValue == null) {
                return -1;
            }
            final int frequency = frequencyAndValue.first;
            final Set<Integer> keys = frequencies.get(frequency);
            keys.remove(key);
            if (minf == frequency && keys.isEmpty()) {
                ++minf;
            }
            final int value = frequencyAndValue.second;
            insert(key, frequency + 1, value);
            return value;
        }

        public void put(int key, int value) {
            if (capacity <= 0) {
                return;
            }
            Pair<Integer, Integer> frequencyAndValue = cache.get(key);
            if (frequencyAndValue != null) {
                cache.put(key, new Pair<>(frequencyAndValue.first, value));
                get(key);
                return;
            }
            if (capacity == cache.size()) {
                final Set<Integer> keys = frequencies.get(minf);
                final int keyToDelete = keys.iterator().next();
                cache.remove(keyToDelete);
                keys.remove(keyToDelete);
            }
            minf = 1;
            insert(key, 1, value);
        }
    }
}