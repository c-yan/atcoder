// Union Find 木
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func find(parent []int, i int) int {
	if parent[i] == -1 {
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
	parent[i] = j
}

func fill(a []int, x int) {
	for i := 0; i < len(a); i++ {
		a[i] = x
	}
}

func main() {
	defer flush()

	n := readInt()
	k := readInt()
	l := readInt()

	roads := make([]int, n)
	fill(roads, -1)
	rails := make([]int, n)
	fill(rails, -1)

	for i := 0; i < k; i++ {
		p := readInt()
		q := readInt()
		unite(roads, p-1, q-1)
	}

	for i := 0; i < l; i++ {
		p := readInt()
		q := readInt()
		unite(rails, p-1, q-1)
	}

	d := map[int]int{}
	for i := 0; i < n; i++ {
		d[2000001*find(roads, i)+find(rails, i)]++
	}

	for i := 0; i < n; i++ {
		println(d[2000001*find(roads, i)+find(rails, i)])
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
