package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func isqrt(n int) int {
	if n < 0 {
		panic("isqrt argument must be nonnegative")
	}

	if n <= 1 {
		return n
	}

	ok := 0
	ng := 3037000500 // 3037000499 * 3037000499 < math.MaxInt64 < 3037000500 * 3037000500
	if n < ng {
		ng = n
	}
	for ng-ok > 1 {
		m := ok + (ng-ok)/2
		if m*m <= n {
			ok = m
		} else {
			ng = m
		}
	}
	return ok
}

func makeDivisorList(n int) []int {
	result := make([]int, 0)
	for i := 1; i <= isqrt(n); i++ {
		if n%i == 0 {
			result = append(result, i, n/i)
		}
	}
	return result
}

func calcMinOps(r []int, d int) int {
	i, j := 0, len(r)
	for i < j && r[i] == 0 {
		i++
	}
	i--
	a, b := 0, 0
	for j-i != 1 {
		if a <= b {
			i++
			a += r[i]
		} else {
			j--
			b += d - r[j]
		}
	}
	return a
}

func main() {
	defer flush()

	N := readInt()
	K := readInt()

	A := make([]int, N)
	c := 0
	for i := 0; i < N; i++ {
		A[i] = readInt()
		c += A[i]
	}
	r := make([]int, N)

	divisors := makeDivisorList(c)
	sort.Sort(sort.Reverse(sort.IntSlice(divisors)))
	for _, d := range divisors {
		for i := 0; i < N; i++ {
			r[i] = A[i] % d
		}
		sort.Ints(r)
		if calcMinOps(r, d) <= K {
			println(d)
			break
		}
	}
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

var stdoutWriter = bufio.NewWriter(os.Stdout)

func flush() {
	stdoutWriter.Flush()
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
