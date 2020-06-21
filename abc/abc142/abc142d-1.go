package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func gcd(x, y int) int {
	if x < y {
		x, y = y, x
	}
	for y > 0 {
		x, y = y, x%y
	}
	return x
}

func main() {
	A := readInt()
	B := readInt()

	N := gcd(A, B)
	if N == 1 {
		fmt.Println(1)
		return
	}

	result := 1
	r := int(math.Sqrt(float64(N)))
	for x := 2; x < r+1; x++ {
		if N%x == 0 {
			result++
			for N%x == 0 {
				N /= x
			}
			if N == 1 {
				break
			}
		}
	}
	if N != 1 {
		result++
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
