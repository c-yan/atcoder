package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	defer flush()

	N := readInt()

	root := -1
	children := make([][]int, N+1)
	left := make([]int, N+1)
	right := make([]int, N+1)

	for i := 1; i <= N; i++ {
		p := readInt()
		if p == -1 {
			root = i
		} else {
			children[p] = append(children[p], i)
		}
	}

	i := 0
	s := []int{root}

	for len(s) != 0 {
		n := s[len(s)-1]
		s = s[:len(s)-1]
		if n > 0 {
			left[n] = i
			i++
			s = append(s, -n)
			for _, c := range children[n] {
				s = append(s, c)
			}
		} else {
			right[-n] = i
			i++
		}
	}

	Q := readInt()
	for i := 0; i < Q; i++ {
		a := readInt()
		b := readInt()
		if left[b] <= left[a] && left[a] <= right[b] {
			println("Yes")
		} else {
			println("No")
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

func readInts(n int) []int {
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = readInt()
	}
	return result
}

var stdoutWriter = bufio.NewWriter(os.Stdout)

func flush() {
	stdoutWriter.Flush()
}

func printf(f string, args ...interface{}) (int, error) {
	return fmt.Fprintf(stdoutWriter, f, args...)
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
