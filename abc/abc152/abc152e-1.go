// エラトステネスの篩, フェルマーの小定理
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	m = 1000000007
)

func mpow(x, y int) int {
	result := 1
	for y != 0 {
		if y&1 == 1 {
			result *= x
			result %= m
		}
		x *= x
		x %= m
		y >>= 1
	}
	return result
}

func makePrimeTable(n int) []int {
	sieve := make([]int, n+1)
	sieve[0] = -1
	sieve[1] = -1
	for i := 2; i <= n; i += 2 {
		sieve[i] = 2
	}
	for i := 3; i <= n; i += 2 {
		if sieve[i] != 0 {
			continue
		}
		sieve[i] = i
		for j := i * i; j <= n; j += i * 2 {
			if sieve[j] == 0 {
				sieve[j] = i
			}
		}
	}
	return sieve
}

func main() {
	maxA := 1000000

	N := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	primeTable := makePrimeTable(maxA)

	lcmFactors := map[int]int{}
	for i := 0; i < N; i++ {
		t := map[int]int{}
		a := A[i]
		for a != 1 {
			t[primeTable[a]]++
			a /= primeTable[a]
		}
		for k, v := range t {
			if lcmFactors[k] < v {
				lcmFactors[k] = v
			}
		}
	}

	lcm := 1
	for k, v := range lcmFactors {
		for i := 0; i < v; i++ {
			lcm *= k
			lcm %= m
		}
	}

	result := 0
	for i := 0; i < N; i++ {
		result += lcm * mpow(A[i], m-2)
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
