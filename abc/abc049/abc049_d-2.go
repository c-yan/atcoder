// BFS(幅優先探索)
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type intQueue []int

func (queue *intQueue) enqueue(i int) {
	*queue = append(*queue, i)
}

func (queue *intQueue) dequeue() int {
	result := (*queue)[0]
	*queue = (*queue)[1:]
	return result
}

func createGroups(n int, links [][]int) []int {
	groups := make([]int, n)
	for i := 0; i < n; i++ {
		groups[i] = i
	}
	var queue intQueue = make([]int, 0)
	for i := 0; i < n; i++ {
		if groups[i] != i {
			continue
		}
		queue.enqueue(i)
		for len(queue) != 0 {
			j := queue.dequeue()
			for _, k := range links[j] {
				if groups[k] != i {
					groups[k] = i
					queue.enqueue(k)
				}
			}
		}
	}
	return groups
}

func readLinks(n, k int) [][]int {
	links := make([][]int, n)
	for i := 0; i < k; i++ {
		p := readInt()
		q := readInt()
		links[p-1] = append(links[p-1], q-1)
		links[q-1] = append(links[q-1], p-1)
	}
	return links
}

func main() {
	defer flush()

	n := readInt()
	k := readInt()
	l := readInt()

	roadLinks := readLinks(n, k)
	railLinks := readLinks(n, l)

	roadGroups := createGroups(n, roadLinks)
	railGroups := createGroups(n, railLinks)

	d := map[int]int{}
	for i := 0; i < n; i++ {
		d[2000001*roadGroups[i]+railGroups[i]]++
	}

	for i := 0; i < n; i++ {
		println(d[2000001*roadGroups[i]+railGroups[i]])
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
