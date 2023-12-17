package com.leetcode;

import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

/**
 * 2353. Design a Food Rating System
 * https://leetcode.com/problems/design-a-food-rating-system/
 */
public class Problem2353 {
    private static class FoodRatings {
        private Map<String, Integer> ratingMap;
        private Map<String, String> cuisineMap;
        private Map<String, PriorityQueue<Food>> cuisineFoodMap;

        public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
            this.ratingMap = new HashMap<>();
            this.cuisineMap = new HashMap<>();
            this.cuisineFoodMap = new HashMap<>();
            for (int i = 0; i < foods.length; i++) {
                ratingMap.put(foods[i], ratings[i]);
                cuisineMap.put(foods[i], cuisines[i]);
                cuisineFoodMap.computeIfAbsent(cuisines[i], k -> new PriorityQueue<>()).add(new Food(ratings[i], foods[i]));
            }
        }

        public void changeRating(String food, int newRating) {
            this.ratingMap.put(food, newRating);
            String name = cuisineMap.get(food);
            cuisineFoodMap.get(name).add(new Food(newRating, food));
        }

        public String highestRated(String cuisine) {
            Food f = cuisineFoodMap.get(cuisine).peek();
            while (ratingMap.get(f.name) != f.rating) {
                cuisineFoodMap.get(cuisine).poll();
                f = cuisineFoodMap.get(cuisine).peek();
            }
            return f.name;
        }
    }

    static class Food implements Comparable<Food> {
        public int rating;
        public String name;

        public Food(int rating, String name) {
            this.rating = rating;
            this.name = name;
        }

        @Override
        public int compareTo(Food that) {
            if (this.rating == that.rating) {
                return this.name.compareTo(that.name);
            }
            return -1 * Integer.compare(this.rating, that.rating);
        }
    }
}
