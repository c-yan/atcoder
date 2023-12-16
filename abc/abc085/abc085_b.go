package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	m := make(map[int]int)
	var d int
	for i := 0; i < n; i++ {
		fmt.Scan(&d)
		m[d] = 0
	}
	fmt.Println(len(m))
}
