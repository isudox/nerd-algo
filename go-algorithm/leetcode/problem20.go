package main

// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

func isValid(s string) bool {
	rp := map[string]bool{")": true, "]": true, "}": true}
	mapper := map[string]string{")": "(", "]": "[", "}": "{"}
	st := make([]string, 0)
	for _, ch := range s {
		str := string(ch)
		if _, ok := rp[str]; !ok {
			st = append(st, str)
		} else {
			if len(st) == 0 {
				return false
			}
			peek := st[len(st)-1]
			if peek != mapper[str] {
				return false
			}
			st = st[:len(st)-1]
		}
	}
	return len(st) == 0
}
