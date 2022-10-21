package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * 901. Online Stock Span
 * https://leetcode.com/problems/online-stock-span/
 */
public class Problem901 {
    static class StockSpanner {
        private final List<Integer> stocks;
        private final List<Integer> spanners;

        public StockSpanner() {
            this.stocks = new ArrayList<>();
            this.spanners = new ArrayList<>();
        }

        public int next(int price) {
            int cnt = 1;
            int n = stocks.size();
            if (n > 0 && stocks.get(n - 1) <= price) {
                int i = n - 1;
                while (i >= 0) {
                    if (stocks.get(i) > price) {
                        break;
                    }
                    cnt += spanners.get(i);
                    i -= spanners.get(i);
                }
            }
            stocks.add(price);
            spanners.add(cnt);
            return cnt;
        }
    }
}
