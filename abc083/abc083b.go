package main

import (
	"fmt"
)

func main() {
	var n, a, b int
	fmt.Scan(&n, &a, &b)
	result := 0
	for i := 1; i <= n; i++ {
		k := 0
		for j := i; j != 0; j /= 10 {
			k += j % 10
		}
		if a <= k && k <= b {
			result += i
		}
	}
	fmt.Println(result)
}
