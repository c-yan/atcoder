package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func isMovable(a string, b string) bool {
	d := 0
	for i := 0; i < len(a); i++ {
		if a[i] == b[i] {
			continue
		}
		d++
		if d > 1 {
			break
		}
	}
	return d == 1
}

func main() {
	defer flush()

	first := readString()
	last := readString()

	if first == last {
		println(0)
		println(first)
		println(last)
		return
	}

	N := readInt()
	s := make([]string, N)
	for i := 0; i < N; i++ {
		s[i] = readString()
	}
	s = append(s, last)

	previous := make(map[string]string)
	previous[first] = ""
	q := make([]string, 0)
	q = append(q, first)
	for len(q) > 0 {
		a := q[0]
		q = q[1:]
		for i := 0; i < len(s); i++ {
			b := s[i]
			if _, ok := previous[b]; ok {
				continue
			}
			if !isMovable(a, b) {
				continue
			}
			q = append(q, b)
			previous[b] = a
		}
	}

	if _, ok := previous[last]; !ok {
		println(-1)
		return
	}

	a := last
	t := make([]string, 0)
	t = append(t, last)
	for previous[a] != "" {
		t = append(t, previous[a])
		a = previous[a]
	}
	println(len(t) - 2)
	for i := 0; i < len(t); i++ {
		println(t[len(t)-1-i])
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
