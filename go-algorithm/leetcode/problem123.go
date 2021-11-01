package main

func maxProfit3(prices []int) int {
	max := func(x, y int) int {
		if x > y {
			return x
		}
		return y
	}
	n := len(prices)
	if n < 2 {
		return 0
	}
	firstBuy, firstSell := -prices[0], 0
	secondBuy, secondSell := -prices[0], 0
	for i := 1; i < n; i++ {
		firstBuy2 := max(firstBuy, -prices[i])
		firstSell2 := max(firstBuy+prices[i], firstSell)
		secondBuy2 := max(secondBuy, firstSell-prices[i])
		secondSell2 := max(secondSell, secondBuy+prices[i])
		firstBuy = firstBuy2
		firstSell = firstSell2
		secondBuy = secondBuy2
		secondSell = secondSell2
	}
	return secondSell
}
