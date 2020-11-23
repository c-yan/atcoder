package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	dp map[int]float64
	N  int
)

func spread(a int) (int, int, int) {
	return a >> 18, (a >> 9) & 255, a & 255
}

func despread(x, y, z int) int {
	return (x << 18) | (y << 9) | z
}

func f(x, y, z int) float64 {
	a := despread(x, y, z)
	if v, ok := dp[a]; ok {
		return v
	}
	if a == 0 {
		return 0
	}

	t := float64(N)
	if x != 0 {
		t += f(x-1, y+1, z) * float64(x)
	}
	if y != 0 {
		t += f(x, y-1, z+1) * float64(y)
	}
	if z != 0 {
		t += f(x, y, z-1) * float64(z)
	}
	dp[a] = t / float64(x+y+z)
	return dp[a]
}

func main() {
	defer flush()

	N = readInt()
	a := make([]int, N)
	for i := 0; i < N; i++ {
		a[i] = readInt()
	}

	var t [4]int
	for i := 0; i < N; i++ {
		t[a[i]]++
	}

	dp = make(map[int]float64, 10000000)
	println(f(t[3], t[2], t[1]))
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
