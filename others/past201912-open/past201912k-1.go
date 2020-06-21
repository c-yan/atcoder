package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

func main() {
	defer flush()

	N := readInt()

	root := -1
	children := make([][]int, N+1)
	parent := make([][]int, 18)
	for i := 0; i < 18; i++ {
		parent[i] = make([]int, N+1)
	}

	for i := 1; i <= N; i++ {
		p := readInt()
		parent[0][i] = p
		if p == -1 {
			root = i
		} else {
			children[p] = append(children[p], i)
		}
	}

	for i := 1; i < 18; i++ {
		for j := 1; j <= N; j++ {
			t := parent[i-1][j]
			if t == -1 {
				parent[i][j] = -1
			} else {
				parent[i][j] = parent[i-1][t]
			}
		}
	}

	depth := make([]int, N+1)
	q := [][2]int{{root, 0}}
	for len(q) != 0 {
		e := q[0]
		q = q[1:]
		n, d := e[0], e[1]
		depth[n] = d
		for _, c := range children[n] {
			q = append(q, [2]int{c, d + 1})
		}
	}

	Q := readInt()
	for i := 0; i < Q; i++ {
		a := readInt()
		b := readInt()
		if depth[a] <= depth[b] {
			println("No")
			continue
		}
		for depth[a] != depth[b] {
			t := int(math.Log2(float64(depth[a] - depth[b])))
			a = parent[t][a]
		}
		if a == b {
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

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
