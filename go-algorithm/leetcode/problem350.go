package leetcode

/*
350. Intersection of Two Arrays II
https://leetcode.com/problems/intersection-of-two-arrays-ii/
*/
func intersect(nums1 []int, nums2 []int) []int {
	var ans []int
	counter1, counter2 := make(map[int]int), make(map[int]int)
	for _, num := range nums1 {
		counter1[num]++
	}
	for _, num := range nums2 {
		counter2[num]++
	}
	for num, cnt := range counter1 {
		if counter2[num] != 0 {
			times := 0
			if cnt < counter2[num] {
				times = cnt
			} else {
				times = counter2[num]
			}
			for i := 0; i < times; i++ {
				ans = append(ans, num)
			}
		}
	}
	return ans
}
