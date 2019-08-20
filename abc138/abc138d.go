package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	n := readInt()
	q := readInt()

	results := make([]int, n)
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
		results[p] += x
	}

	processed := make([]bool, n)
	processed[0] = true
	queue := make([]int, 0)
	queue = append(queue, 0)
	for len(queue) != 0 {
		i := queue[0]
		queue = queue[1:]
		for _, j := range links[i] {
			if processed[j] {
				continue
			}
			results[j] += results[i]
			processed[j] = true
			queue = append(queue, j)
		}
	}

	printIntln(results...)
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
