package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func gcd(x, y int) int {
	if y == 0 {
		return x
	}
	return gcd(y, x%y)
}

func primeFactorize(n int) [][2]int {
	var result [][2]int
	rn := int(math.Sqrt(float64(n)))
	for i := 2; i < rn+1; i++ {
		if n%i != 0 {
			continue
		}
		t := [2]int{i, 0}
		for n%i == 0 {
			n /= i
			t[1]++
		}
		result = append(result, t)
	}
	if n != 1 {
		result = append(result, [2]int{n, 1})
	}
	return result
}

func main() {
	A := readInt()
	B := readInt()

	fmt.Println(len(primeFactorize(gcd(A, B))) + 1)
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
