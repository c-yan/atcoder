package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	N := readInt()
	S := readString()
	ms := 0
	for i := 1; i < N; i++ {
		ts := 0
		for j := 0; j < N-i; j++ {
			if S[j] == S[j+i] {
				ts++
				if ts > ms {
					ms = ts
				}
				if ts == i {
					break
				}
			} else {
				ts = 0
			}
		}
	}
	fmt.Println(ms)
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
