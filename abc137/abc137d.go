package main

import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"strconv"
)

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func main() {
	n := readInt()
	m := readInt()

	jobs := map[int][]int{}
	for i := 0; i < n; i++ {
		a := readInt()
		b := readInt()
		jobs[a] = append(jobs[a], b)
	}

	result := 0
	candidates := &IntHeap{}
	heap.Init(candidates)
	for i := 1; i < m+1; i++ {
		_, ok := jobs[i]
		if ok {
			for _, j := range jobs[i] {
				heap.Push(candidates, -j)
			}
		} else {
			if candidates.Len() == 0 {
				continue
			}
		}
		result += -heap.Pop(candidates).(int)
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
