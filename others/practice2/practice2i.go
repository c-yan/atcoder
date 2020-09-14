package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func makeSuffixArray(s string) []int {
	n := len(s)
	sa := make([]int, n)
	for i := 0; i < n; i++ {
		sa[i] = i
	}
	rnk := make([]int, n)
	for i, b := range []byte(s) {
		rnk[i] = int(b)
	}
	tmp := make([]int, n)

	for k := 1; k < n; k *= 2 {
		cmp := func(x, y int) bool {
			if rnk[sa[x]] != rnk[sa[y]] {
				return rnk[sa[x]] < rnk[sa[y]]
			}
			rx, ry := -1, -1
			if sa[x]+k < n {
				rx = rnk[sa[x]+k]
			}
			if sa[y]+k < n {
				ry = rnk[sa[y]+k]
			}
			return rx < ry
		}
		sort.Slice(sa, cmp)
		tmp[sa[0]] = 0
		for i := 1; i < n; i++ {
			tmp[sa[i]] = tmp[sa[i-1]]
			if cmp(i-1, i) {
				tmp[sa[i]]++
			}
		}
		tmp, rnk = rnk, tmp
	}
	return sa
}

func makeLcpArray(s string, sa []int) []int {
	b := []byte(s)
	n := len(s)
	rnk := make([]int, n)
	for i := 0; i < n; i++ {
		rnk[sa[i]] = i
	}
	lcp := make([]int, n-1)
	h := 0
	for i := 0; i < n; i++ {
		if h > 0 {
			h--
		}
		if rnk[i] == 0 {
			continue
		}
		j := sa[rnk[i]-1]
		for j+h < n && i+h < n {
			if b[j+h] != b[i+h] {
				break
			}
			h++
		}
		lcp[rnk[i]-1] = h
	}
	return lcp
}

func main() {
	defer flush()

	S := readString()
	sa := makeSuffixArray(S)

	result := len(S) * (len(S) + 1) / 2
	for _, x := range makeLcpArray(S, sa) {
		result -= x
	}
	println(result)
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
