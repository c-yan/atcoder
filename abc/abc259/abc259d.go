package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	N int
	x []int
	y []int
	r []int
)

func find(parent []int, i int) int {
	if parent[i] < 0 {
		return i
	}
	parent[i] = find(parent, parent[i])
	return parent[i]
}

func unite(parent []int, i, j int) {
	i = find(parent, i)
	j = find(parent, j)
	if i == j {
		return
	}
	parent[j] += parent[i]
	parent[i] = j
}

func dist(x1, y1, x2, y2 int) int {
	return (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
}

func intersect(i, j int) bool {
	return (dist(x[i], y[i], x[j], y[j]) >= (r[i]-r[j])*(r[i]-r[j])) && (dist(x[i], y[i], x[j], y[j]) <= (r[i]+r[j])*(r[i]+r[j]))
}

func onCircle(x1, y1, i int) bool {
	return (x1-x[i])*(x1-x[i])+(y1-y[i])*(y1-y[i]) == r[i]*r[i]
}

func getCircleNumber(x1, y1 int) int {
	for i := 0; i < N; i++ {
		if onCircle(x1, y1, i) {
			return i
		}
	}
	return -1
}

func main() {
	defer flush()

	N = readInt()
	sx := readInt()
	sy := readInt()
	tx := readInt()
	ty := readInt()

	x = make([]int, N)
	y = make([]int, N)
	r = make([]int, N)

	for i := 0; i < N; i++ {
		x[i] = readInt()
		y[i] = readInt()
		r[i] = readInt()
	}

	parent := make([]int, N)
	for i := 0; i < N; i++ {
		parent[i] = -1
	}

	for i := 0; i < N-1; i++ {
		for j := i + 1; j < N; j++ {
			if intersect(i, j) {
				unite(parent, i, j)
			}
		}
	}

	if find(parent, getCircleNumber(sx, sy)) == find(parent, getCircleNumber(tx, ty)) {
		println("Yes")
	} else {
		println("No")
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
