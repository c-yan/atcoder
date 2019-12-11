package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	const m = 1000000007

	N := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	result := 0
	for bit := 0; bit < 60; bit++ {
		bitSum := 0
		for i := 0; i < N; i++ {
			bitSum += A[i] & 1 // bitSum <= 3 * 10^5
			A[i] >>= 1
		}

		t := bitSum * (N - bitSum) // t <= 2.25 * 10^10
		t %= m
		t *= (1 << uint(bit)) % m
		t %= m

		result += t
		result %= m
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
