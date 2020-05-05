package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	N := readInt()
	S := readString()

	result := 0
	for i := N - 1; i > 0; i-- {
		if i <= result {
			break
		}
		t := 0
		for j := 0; j < N-i; j++ {
			if S[j] == S[j+i] {
				t++
				result = max(result, t)
				if result == i {
					break
				}
			} else {
				t = 0
			}
		}
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

func readInt() int {
	result, err := strconv.Atoi(readString())
	if err != nil {
		panic(err)
	}
	return result
}
