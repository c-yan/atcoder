package main

import (
	"fmt"
)

func StartsWith(s, prefix []rune) bool {
	if len(s) < len(prefix) {
		return false
	}
	for i := range prefix {
		if s[i] != prefix[i] {
			return false
		}
	}
	return true
}

func main() {
	var s string
	fmt.Scanln(&s)
	r := []rune(s)
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	words := [][]rune{[]rune("maerd"), []rune("remaerd"), []rune("esare"), []rune("resare")}
	for {
		if len(r) == 0 {
			fmt.Println("YES")
			return
		}
		fail := 0
		for _, w := range words {
			if StartsWith(r, w) {
				r = r[len(w):]
				break
			} else {
				fail++
			}
		}
		if fail == len(words) {
			fmt.Println("NO")
			return
		}
	}
}
