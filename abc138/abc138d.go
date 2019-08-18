package main

import (
	"bufio"
	"os"
	"strconv"
)

type task struct {
	Current int
	Parent  int
}

func main() {
	n := readInt()
	q := readInt()

	results := make([]int, n)
	links := make([][]int, n)

	for i := 0; i < n-1; i++ {
		a := readInt() - 1
		b := readInt() - 1
		links[a] = append(links[a], b)
		links[b] = append(links[b], a)
	}

	for i := 0; i < q; i++ {
		p := readInt() - 1
		x := readInt()
		results[p] += x
	}

	queue := make([]task, 0)
	queue = append(queue, task{0, -1})
	for len(queue) != 0 {
		t := queue[0]
		queue = queue[1:]
		for _, j := range links[t.Current] {
			if t.Parent == j {
				continue
			}
			results[j] += results[t.Current]
			queue = append(queue, task{j, t.Current})
		}
	}

	for i := 0; i < n; i++ {
		writeInt(results[i])
		if i != n {
			writeString(" ")
		}
	}
	writeNewLineAndFlush()
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

var stdoutWriter = bufio.NewWriter(os.Stdout)

func readString() string {
	stdinScanner.Scan()
	return stdinScanner.Text()
}

func readInt() int {
	result, _ := strconv.Atoi(readString())
	return result
}

func writeString(s string) {
	stdoutWriter.WriteString(s)
}

func writeInt(i int) {
	writeString(strconv.Itoa(i))
}

func writeNewLineAndFlush() {
	stdoutWriter.WriteString("\n")
	stdoutWriter.Flush()
}
