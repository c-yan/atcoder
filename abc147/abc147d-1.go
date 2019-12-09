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
	a := make([]int, N)
	bs := make([]int, N)
	for b := 0; b < 60; b++ {
		for i := 0; i < N; i++ {
			a[i] = (A[i] >> uint(b)) & 1
		}

		bs[N-1] = a[N-1]
		for i := N - 2; i > -1; i-- {
			bs[i] = bs[i+1] + a[i]
		}

		t := 0
		for i := 0; i < N-1; i++ {
			if a[i] == 0 {
				t += bs[i+1]
			} else {
				t += (N - (i + 1)) - bs[i+1]
			}
		}
		t %= m

		v := (1 << uint(b)) % m
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
