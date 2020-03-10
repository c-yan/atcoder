package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	L := readString()

	result := 1
	t := 1
	for i := len(L) - 1; i >= 0; i-- {
		if L[i] == '1' {
			result = result*2 + t
			result %= 1000000007
		}
		t *= 3
		t %= 1000000007
	}
	fmt.Println(result)
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
