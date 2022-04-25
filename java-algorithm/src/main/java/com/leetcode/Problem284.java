package com.leetcode;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * 284. Peeking Iterator
 * https://leetcode.com/problems/peeking-iterator/
 */
public class Problem284 {
    private static class PeekingIterator implements Iterator<Integer> {
        private final List<Integer> list;
        private int idx = 0;
        public PeekingIterator(Iterator<Integer> iterator) {
            this.list = new ArrayList<>();
            while (iterator.hasNext()) {
                list.add(iterator.next());
            }
        }
        public Integer peek() {
            return list.get(idx);
        }

        @Override
        public Integer next() {
            return list.get(idx++);
        }

        @Override
        public boolean hasNext() {
            return idx < list.size();
        }
    }
}
