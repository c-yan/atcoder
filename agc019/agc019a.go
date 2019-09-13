package main

import (
	"fmt"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func f(n int, l float64, price map[float64]int) int {
	t := int(float64(n) / l)
	if l == 0.25 {
		return t * price[l]
	}
	return min(f(n-int(l*float64(t)), l/2, price)+t*price[l], f(n, l/2, price))
}

func main() {
	var Q, H, S, D int
	fmt.Scan(&Q, &H, &S, &D)
	var N int
	fmt.Scan(&N)
	price := map[float64]int{0.25: Q, 0.5: H, 1.0: S, 2.0: D}
	fmt.Println(f(N, 2.0, price))
}
