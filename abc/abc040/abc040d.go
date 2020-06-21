// Union Find 木
package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
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

func fill(a []int, x int) {
	for i := 0; i < len(a); i++ {
		a[i] = x
	}
}

type aby struct{ a, b, y int }
type byY []aby

func (a byY) Len() int           { return len(a) }
func (a byY) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a byY) Less(i, j int) bool { return a[i].y > a[j].y }

type wvi struct{ w, v, i int }
type byW []wvi

func (a byW) Len() int           { return len(a) }
func (a byW) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a byW) Less(i, j int) bool { return a[i].w > a[j].w }

func main() {
	defer flush()

	N := readInt()
	M := readInt()
	roads := make([]aby, M)
	for i := 0; i < M; i++ {
		roads[i].a = readInt() - 1
		roads[i].b = readInt() - 1
		roads[i].y = readInt()
	}
	Q := readInt()
	citizen := make([]wvi, Q)
	for i := 0; i < Q; i++ {
		citizen[i].v = readInt() - 1
		citizen[i].w = readInt()
		citizen[i].i = i
	}

	parent := make([]int, N)
	fill(parent, -1)

	sort.Sort(byY(roads))
	sort.Sort(byW(citizen))

	result := make([]int, Q)
	t := 0
	for i := 0; i < Q; i++ {
		c := citizen[i]
		for t < len(roads) && roads[t].y > c.w {
			unite(parent, find(parent, roads[t].a), find(parent, roads[t].b))
			t++
		}
		result[c.i] = -parent[find(parent, c.v)]
	}
	for i := 0; i < Q; i++ {
		println(result[i])
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

func printf(f string, args ...interface{}) (int, error) {
	return fmt.Fprintf(stdoutWriter, f, args...)
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
