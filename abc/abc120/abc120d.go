// Union Find 木
package main

import (
	"bufio"
	"fmt"
	"os"
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

func reverseInts(a []int) {
	l := len(a)
	for i := 0; i < l/2; i++ {
		a[i], a[l-1-i] = a[l-1-i], a[i]
	}
}

func main() {
	N := readInt()
	M := readInt()
	AB := make([]struct{ A, B int }, M)
	for i := 0; i < M; i++ {
		AB[i].A = readInt() - 1
		AB[i].B = readInt() - 1
	}

	parent := make([]int, N)
	for i := 0; i < N; i++ {
		parent[i] = -1
	}
	inconvenience := N * (N - 1) / 2
	var result []int
	for i := M - 1; i > -1; i-- {
		a := AB[i].A
		b := AB[i].B
		result = append(result, inconvenience)
		pa := find(parent, a)
		pb := find(parent, b)
		if pa != pb {
			inconvenience -= parent[pa] * parent[pb]
		}
		unite(parent, a, b)
	}

	reverseInts(result)
	printIntln(result...)
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

func printIntln(v ...int) {
	b := make([]byte, 0, 4096)
	for i := 0; i < len(v)-1; i++ {
		b = append(b, strconv.Itoa(v[i])...)
		b = append(b, " "...)
	}
	b = append(b, strconv.Itoa(v[len(v)-1])...)
	fmt.Println(string(b))
}
