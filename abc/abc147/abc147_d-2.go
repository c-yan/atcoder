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
		t := 0
		bitSum := (A[N-1] >> uint(bit)) & 1
		for i := N - 2; i > -1; i-- {
			if (A[i]>>uint(bit))&1 == 0 {
				t += bitSum
			} else {
				t += (N - (i + 1)) - bitSum
				bitSum++
			}
		}
		t %= m
		v := (1 << uint(bit)) % m
		result += (t * v) % m
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
