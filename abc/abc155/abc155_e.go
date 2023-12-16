package main

import (
	"bufio"
	"fmt"
	"os"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	N := readString()

	b := []byte(N)
	x, y := 0, 0

	t := int(b[len(b)-1] - '0')
	x, y = x+t, y+(10-t)

	for i := len(b) - 2; i >= 0; i-- {
		t := int(b[i] - '0')
		x, y = min(x+t, y+(t+1)), min(x+(10-t), y+(10-(t+1)))
	}
	fmt.Println(min(x, y+1))
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
