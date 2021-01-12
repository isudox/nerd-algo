package com.common;

import java.util.Map;

public class UnionFind<E> {

    private Map<E, E> parent;

    public UnionFind() {
    }

    public void union(E x, E y) {
        parent.put(find(x), find(y));
    }

    public E find(E arg) {
        if (parent.get(arg) != arg) {
            parent.put(arg, find(parent.get(arg)));
        }
        return parent.get(arg);
    }
}
