package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"math"
	"os"
	"strconv"
)

type node struct {
	y, x, c int
}
type nodeHeap []node

func (h nodeHeap) Len() int           { return len(h) }
func (h nodeHeap) Less(i, j int) bool { return h[i].c < h[j].c }
func (h nodeHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *nodeHeap) Push(x interface{}) {
	*h = append(*h, x.(node))
}

func (h *nodeHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

//
var (
	H int
	W int
	A [][]int
)

func costFrom(y1, x1 int) [][]int {
	dp := make([][]int, H)
	for i := 0; i < H; i++ {
		dp[i] = make([]int, W)
		for j := 0; j < W; j++ {
			dp[i][j] = math.MaxInt64
		}
	}

	dp[y1][x1] = 0
	q := &nodeHeap{{y1, x1, 0}}
	heap.Init(q)
	for len(*q) != 0 {
		n := heap.Pop(q).(node)
		y, x, c := n.y, n.x, n.c
		t := dp[y][x]
		if t != c {
			continue
		}
		if y-1 >= 0 {
			u := t + A[y-1][x]
			if dp[y-1][x] > u {
				dp[y-1][x] = u
				heap.Push(q, node{y - 1, x, u})
			}
		}
		if y+1 < H {
			u := t + A[y+1][x]
			if dp[y+1][x] > u {
				dp[y+1][x] = t + A[y+1][x]
				heap.Push(q, node{y + 1, x, u})
			}
		}
		if x-1 >= 0 {
			u := t + A[y][x-1]
			if dp[y][x-1] > u {
				dp[y][x-1] = u
				heap.Push(q, node{y, x - 1, u})
			}
		}
		if x+1 < W {
			u := t + A[y][x+1]
			if dp[y][x+1] > u {
				dp[y][x+1] = u
				heap.Push(q, node{y, x + 1, u})
			}
		}
	}
	return dp
}

func main() {
	H = readInt()
	W = readInt()
	A = make([][]int, H)
	for i := 0; i < H; i++ {
		A[i] = make([]int, W)
		for j := 0; j < W; j++ {
			A[i][j] = readInt()
		}
	}

	result := math.MaxInt64
	cost1 := costFrom(H-1, 0)
	cost2 := costFrom(H-1, W-1)
	cost3 := costFrom(0, W-1)
	for i := 0; i < H; i++ {
		for j := 0; j < W; j++ {
			t := cost1[i][j] + cost2[i][j] + cost3[i][j] - 2*A[i][j]
			if t < result {
				result = t
			}
		}
	}
	fmt.Println(result)
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
