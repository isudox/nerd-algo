package main

// 383. Ransom Note
// https://leetcode.com/problems/ransom-note/

func canConstruct(ransomNote string, magazine string) bool {
	counter1 := make(map[int32]int)
	for _, ch := range ransomNote {
		counter1[ch]++
	}
	counter2 := make(map[int32]int)
	for _, ch := range magazine {
		counter2[ch]++
	}
	for ch, cnt := range counter1 {
		if counter2[ch] < cnt {
			return false
		}
	}
	return true
}
