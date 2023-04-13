package main

func maxNumberOfBalloons(text string) int {
	counter := make(map[uint8]int)
	for i := 0; i < len(text); i++ {
		c := text[i]
		if c == 'b' || c == 'a' || c == 'n' {
			counter[c] += 2
		}
		if c == 'l' || c == 'o' {
			counter[c] += 1
		}
	}
	ans := len(text)
	for _, v := range "balon" {
		if counter[uint8(v)] < ans {
			ans = counter[uint8(v)]
		}
	}
	return ans / 2
}
