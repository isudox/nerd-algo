package com.leetcode.cn;

import java.util.ArrayList;
import java.util.List;

public class Lcof {

    public int translateNum(int num) {
        String str = String.valueOf(num);
        int length = str.length();
        List<Integer> store = new ArrayList<>(length + 1);
        for (int i = 0; i < length + 1; i++) {
            store.add(1);
        }

        for (int i = length - 2; i >= 0; i--) {
            // f(n) = f(n+1) + (if exists ? f(n+2) : 0)
            store.set(i, store.get(i + 1));
            int temp = Integer.parseInt(str.substring(i, i + 2));
            if (temp < 26 && temp > 9) {
                store.set(i, store.get(i + 1) + store.get(i + 2));
            }
        }

        return store.get(0);
    }

}
