package main

import (
	"fmt"
	"sort"
)

func main() {
	var n int
	fmt.Scan(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}
	sort.Sort(sort.Reverse(sort.IntSlice(a)))
	result := 0
	for i := 0; i < n; i++ {
		if i&1 == 0 {
			result += a[i]

		} else {
			result -= a[i]
		}
	}
	fmt.Println(result)
}
