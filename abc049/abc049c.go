package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var words = []string{"maerd", "remaerd", "esare", "resare"}

func reverseString(s string) string {
	t := make([]byte, len(s))
	for i, b := range []byte(s) {
		t[len(s)-1-i] = b
	}
	return string(t)
}

func main() {
	s := reverseString(readString())

	for {
	next:
		if s == "" {
			fmt.Println("YES")
			return
		}
		for _, w := range words {
			if strings.HasPrefix(s, w) {
				s = s[len(w):]
				goto next
			}
		}
		fmt.Println("NO")
		return
	}
}

const (
	ioBufferSize = 1 * 1024 * 1024 // 1 MB
)

var stdinScanner = func() *bufio.Scanner {
	result := bufio.NewScanner(os.Stdin)
	result.Buffer(make([]byte, ioBufferSize), ioBufferSize)
	result.Split(bufio.ScanWords)
	return result
}()

func readString() string {
	stdinScanner.Scan()
	return stdinScanner.Text()
}
