package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	A := readInt()
	B := readInt()
	X := readInt()

	isOk := func(N int) bool {
		return A*N+B*len(strconv.Itoa(N)) <= X
	}

	ok := 0
	ng := 1000000001
	for ng-ok != 1 {
		m := ok + (ng-ok)/2
		if isOk(m) {
			ok = m
		} else {
			ng = m
		}
	}
	fmt.Println(ok)
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
