package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	result := 0
	for {
		for i := 0; i < n; i++ {
			if a[i]%2 == 1 {
				fmt.Println(result)
				return
			}
			a[i] >>= 1
		}
		result++
	}
}
