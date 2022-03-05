package main

import (
	"encoding/json"
	"fmt"
	"time"
)

// 413. Arithmetic Slices
// https://leetcode.com/problems/arithmetic-slices/

func numberOfArithmeticSlices(nums []int) int {
	n := len(nums)
	if n < 3 {
		return 0
	}
	ans := 0
	for i := 0; i < n-2; i++ {
		d := nums[i+1] - nums[i]
		j := i + 2
		for j < n && nums[j]-nums[j-1] == d {
			j++
		}
		if j-i >= 3 {
			ans += j - i - 2
		}
	}
	return ans
}

type Person struct {
	Name string
}

type School struct {
	Extension *string
}

func change(person *Person) {
	person.Name = "BBB"
}

func main() {
	p := &Person{
		Name: "AAA",
	}

	ext := make(map[string]interface{})
	ext["name"] = p.Name
	extBody, _ := json.Marshal(ext)
	extStr := string(extBody)

	sch := &School{
		Extension: &extStr,
	}
	go change(p)
	time.Sleep(time.Second * 1)
	println(fmt.Sprintf("%+v", *sch.Extension))
}
