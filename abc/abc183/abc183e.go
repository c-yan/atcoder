package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const (
	m = 1000000007
)

func main() {
	defer flush()

	H := readInt()
	W := readInt()
	S := make([]string, H)
	for i := 0; i < H; i++ {
		S[i] = readString()
	}

	au := make([]int, W)
	aul := make([]int, H+W+1)
	t := 0
	for h := 0; h < H; h++ {
		al := 0
		for w := 0; w < W; w++ {
			n := h - w + (W - 1)

			if h == 0 && w == 0 {
				al = 1
				au[w] = 1
				aul[n] = 1
				continue
			}

			if S[h][w] == '#' {
				al = 0
				au[w] = 0
				aul[n] = 0
				continue
			}

			t = al + au[w] + aul[n]
			al += t
			al %= m
			au[w] += t
			au[w] %= m
			aul[n] += t
			aul[n] %= m
		}
	}
	println(t % m)
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
