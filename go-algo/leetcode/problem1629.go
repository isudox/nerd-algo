package main

// 1629. Slowest Key
// https://leetcode.com/problems/slowest-key/

func slowestKey(releaseTimes []int, keysPressed string) byte {
	pos := 0
	time := releaseTimes[0]
	for i := len(releaseTimes) - 1; i > 0; i-- {
		releaseTimes[i] = releaseTimes[i] - releaseTimes[i-1]
		if releaseTimes[i] > time || (releaseTimes[i] == time && keysPressed[i] > keysPressed[pos]) {
			pos = i
			time = releaseTimes[pos]
		}
	}
	return keysPressed[pos]
}
