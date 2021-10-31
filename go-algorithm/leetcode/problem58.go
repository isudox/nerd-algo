package leetcode

func lengthOfLastWord(s string) int {
	n := len(s)
	start, end := 0, n-1
	flag := false
	for i := n - 1; i >= 0; i-- {
		if !flag {
			if s[i] == ' ' {
				continue
			}
			end = i
			flag = true
		}
		if flag {
			if s[i] != ' ' {
				continue
			}
			start = i + 1
			break
		}
	}
	return end - start + 1
}
