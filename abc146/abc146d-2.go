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

func dfs(current, usedColor, from int) {
	color := 1
	for _, e := range edges[current] {
		if e.To == from {
			continue
		}
		if color == usedColor {
			color++
		}
		colors[e.ID] = color
		dfs(e.To, color, current)
		color++
	}
}

func main() {
	N := readInt()

	edges = make([][]edge, N)
	for i := 0; i < N-1; i++ {
		a := readInt() - 1
		b := readInt() - 1
		edges[a] = append(edges[a], edge{To: b, ID: i})
		edges[b] = append(edges[b], edge{To: a, ID: i})
	}

	colors = make([]int, N)
	dfs(0, -1, -1)

	K := -1
	for _, color := range colors {
		if color > K {
			K = color
		}
	}
	fmt.Println(K)

	for i := 0; i < N-1; i++ {
		fmt.Println(colors[i])
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