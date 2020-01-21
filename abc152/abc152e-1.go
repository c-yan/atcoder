// エラトステネスの篩, フェルマーの小定理
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func mpow(x int, n int) int {
	result := 1
	for n != 0 {
		if n&1 == 1 {
			result *= x
			result %= 1000000007
		}
		x *= x
		x %= 1000000007
		n >>= 1
	}
	return result
}

func main() {
	maxA := 1000000

	N := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	sieve := make([]int, maxA+1)
	sieve[0] = -1
	sieve[1] = -1
	for i := 2; i <= maxA; i++ {
		if sieve[i] != 0 {
			continue
		}
		sieve[i] = i
		for j := i * i; j <= maxA; j += i {
			if sieve[j] == 0 {
				sieve[j] = i
			}
		}
	}

	lcmFactors := map[int]int{}
	for i := 0; i < N; i++ {
		t := map[int]int{}
		a := A[i]
		for a != 1 {
			t[sieve[a]]++
			a /= sieve[a]
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
			lcm %= 1000000007
		}
	}

	result := 0
	for i := 0; i < N; i++ {
		result += lcm * mpow(A[i], 1000000007-2)
		result %= 1000000007
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
