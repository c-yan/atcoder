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

func main() {
	defer flush()

	n := readInt()
	q := readInt()

	result := make([]int, n)
	links := make([][]int, n)

	for i := 0; i < n-1; i++ {
		a := readInt() - 1
		b := readInt() - 1
		links[a] = append(links[a], b)
		links[b] = append(links[b], a)
	}

	for i := 0; i < q; i++ {
		p := readInt() - 1
		x := readInt()
		result[p] += x
	}

	processed := make([]bool, n)
	processed[0] = true
	var queue intQueue = make([]int, 0)
	queue.enqueue(0)
	for len(queue) != 0 {
		i := queue.dequeue()
		for _, j := range links[i] {
			if processed[j] {
				continue
			}
			result[j] += result[i]
			processed[j] = true
			queue.enqueue(j)
		}
	}

	for i := 0; i < len(result); i++ {
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

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
