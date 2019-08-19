package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	v := make([]int, n)
	c := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&v[i])
	}
	for i := 0; i < n; i++ {
		fmt.Scan(&c[i])
	}
	var result int
	for i := 0; i < n; i++ {
		if v[i] > c[i] {
			result += v[i] - c[i]
		}
	}
	fmt.Println(result)
}
