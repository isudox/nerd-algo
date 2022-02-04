package main

// 122. Best Time to Buy and Sell Stock II
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

func maxProfit(prices []int) int {
	ans := 0
	i := 0
	for i < len(prices) {
		j := i + 1
		for j < len(prices) && prices[j] > prices[j-1] {
			j++
		}
		ans += prices[j-1] - prices[i]
		i = j
	}
	return ans
}
