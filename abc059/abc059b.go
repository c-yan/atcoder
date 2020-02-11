package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	A := readString()
	B := readString()

	if len(A) > len(B) {
		fmt.Println("GREATER")
	} else if len(A) < len(B) {
		fmt.Println("LESS")
	} else {
		if A > B {
			fmt.Println("GREATER")
		} else if A < B {
			fmt.Println("LESS")
		} else {
			fmt.Println("EQUAL")
		}
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
