package com.leetcode;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * 341. Flatten Nested List Iterator
 */
public class Problem341 {

    private interface NestedInteger {

        // @return true if this NestedInteger holds a single integer, rather than a nested list.
        boolean isInteger();

        // @return the single integer that this NestedInteger holds, if it holds a single integer
        // Return null if this NestedInteger holds a nested list
        Integer getInteger();

        // @return the nested list that this NestedInteger holds, if it holds a nested list
        // Return empty list if this NestedInteger holds a single integer
        List<NestedInteger> getList();
    }

    private static class NestedIterator implements Iterator<Integer> {

        private List<Integer> list;
        private Iterator<Integer> iterator;

        public NestedIterator(List<NestedInteger> nestedList) {
            list = new ArrayList<>();
            dfs(nestedList);
            iterator = list.iterator();
        }

        @Override
        public Integer next() {
            return iterator.next();
        }

        @Override
        public boolean hasNext() {
            return iterator.hasNext();
        }

        private void dfs(List<NestedInteger> nestedIntegers) {
            for (NestedInteger integer : nestedIntegers) {
                if (integer.isInteger()) {
                    list.add(integer.getInteger());
                } else {
                    dfs(integer.getList());
                }
            }
        }
    }
}
