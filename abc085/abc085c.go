package main

import (
	"fmt"
)

func main() {
	var n, y int
	fmt.Scan(&n, &y)
	y /= 1000
	for i := 0; i <= n; i++ {
		for j := 0; j <= n-i; j++ {
			k := n - i - j
			if i*10+j*5+k == y {
				fmt.Println(i, j, k)
				return
			}
		}
	}
	fmt.Println(-1, -1, -1)
}
