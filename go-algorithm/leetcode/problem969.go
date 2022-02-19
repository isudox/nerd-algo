package main

// 969. Pancake Sorting
// https://leetcode.com/problems/pancake-sorting/

func pancakeSort(arr []int) []int {
    ans := make([]int, 0)
    for i := len(arr); i > 1; i-- {
        idx := 0
        for j := 0; j < i; j++ {
            if arr[j] > arr[idx] {
                idx = j
            }
        }
        if idx == i-1 {
            continue
        }
        for j, m := 0, idx; j < (m+1)/2; j++ {
            arr[j], arr[m-j] = arr[m-j], arr[j]
        }
        for j := 0; j < i/2; j++ {
            arr[j], arr[i - 1- j] = arr[i - 1 - j], arr[j]
        }
        ans = append(ans, idx+1, i)
    }
    return ans
}
