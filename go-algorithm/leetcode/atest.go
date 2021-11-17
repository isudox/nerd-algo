package main

import (
	"fmt"
	"reflect"
)

// 定义结构体
type dummy struct {
	a int
	b string

	// 嵌入字段
	float32
	bool

	next *dummy
}

type MyData struct {
	One   int64
	Two   string
	Three int
}

func main() {
	in := &MyData{One: 1, Two: "second"}
	in2 := &MyData{One: 2, Two: "second"}
	fmt.Printf("euqals:%v", reflect.DeepEqual(in.Two, in2.Two))
}
