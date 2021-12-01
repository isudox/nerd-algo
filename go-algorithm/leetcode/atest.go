package main

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
