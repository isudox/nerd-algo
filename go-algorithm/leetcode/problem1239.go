package leetcode

//1239. Maximum Length of a Concatenated String with Unique Characters
//https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
func maxLength(arr []string) int {
	for i, str := range arr {
		if !check(str) {
			arr[i] = ""
		}
	}
	var dfs func(i int, seen []bool) int
	dfs = func(i int, seen []bool) int {
		if i == len(arr) {
			return 0
		}
		if arr[i] == "" {
			return dfs(i+1, seen)
		}
		ret := 0
		valid := true
		for _, c := range arr[i] {
			if seen[c-'a'] {
				valid = false
				break
			}
		}
		if valid {
			for _, c := range arr[i] {
				seen[c-'a'] = true
			}
			ret = dfs(i+1, seen) + len(arr[i])
			for _, c := range arr[i] {
				seen[c-'a'] = false
			}
		}
		ret2 := dfs(i + 1, seen)
		if ret2 > ret {
			ret = ret2
		}
		return ret
	}
	var seen = make([]bool, 26)
	return dfs(0, seen)
}

func check(str string) bool {
	var seen = make([]bool, 26)
	for i := 0; i < len(str); i++ {
		if seen[str[i]-'a'] {
			return false
		}
		seen[str[i]-'a'] = true
	}
	return true
}
