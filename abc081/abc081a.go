package main

import (
	"fmt"
)

func main() {
	var s string
	fmt.Scan(&s)
	result := 0
	for _, c := range s {
		if c == '1' {
			result++
		}
	}
	fmt.Println(result)
}
