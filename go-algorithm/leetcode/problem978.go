package leetcode

func maxTurbulenceSize(arr []int) int {
	n := len(arr)
	ans := 1
	i := 0
	for i < n && n-i > ans {
		j := i + 1
		for j < n && arr[j] == arr[j-1] {
			j++
		}
		if j == n {
			break
		}
		i = j - 1
		j++
		for j < n {
			if arr[j] == arr[j-1] || (arr[j] > arr[j-1]) == (arr[j-1] > arr[j-2]) {
				break
			}
			j++
		}
		if j-i > ans {
			ans = j - i
		}
		i = j - 1
	}
	return ans
}
