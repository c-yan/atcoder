// 深さ優先探索
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type edge struct {
	To int
	ID int
}

var (
	edges  [][]edge
	colors []int
)

func main() {
	defer flush()

	N := readInt()

	edges = make([][]edge, N)
	for i := 0; i < N-1; i++ {
		a := readInt() - 1
		b := readInt() - 1
		edges[a] = append(edges[a], edge{To: b, ID: i})
		edges[b] = append(edges[b], edge{To: a, ID: i})
	}

	colors = make([]int, N)
	q := make([][3]int, 1, N)
	q = append(q, [3]int{0, -1, -1})
	for len(q) != 0 {
		current, usedColor, from := q[len(q)-1][0], q[len(q)-1][1], q[len(q)-1][2]
		q = q[:len(q)-1]
		color := 1
		for _, e := range edges[current] {
			if e.To == from {
				continue
			}
			if color == usedColor {
				color++
			}
			colors[e.ID] = color
			q = append(q, [3]int{e.To, color, current})
			color++
		}
	}

	K := -1
	for _, color := range colors {
		if color > K {
			K = color
		}
	}
	println(K)

	for i := 0; i < N-1; i++ {
		println(colors[i])
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
