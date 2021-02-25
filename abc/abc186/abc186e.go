package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func gcd(x, y int) int {
	if x < 0 {
		x = -x
	}
	if y < 0 {
		y = -y
	}
	if x < y {
		x, y = y, x
	}
	for y > 0 {
		x, y = y, x%y
	}
	return x
}

func divmod(a, b int) (x int, y int) {
	if b < 0 {
		a, b = -a, -b
	}
	if a < 0 {
		x = (a - (b - 1)) / b
	} else {
		x = a / b
	}
	y = a - b*x
	return
}

func div(a, b int) int {
	x, _ := divmod(a, b)
	return x
}

func mod(a, b int) int {
	_, x := divmod(a, b)
	return x
}

func invmod(a, n int) int {
	b, c, m := 1, 0, n
	for n != 0 {
		q, r := divmod(a, n)
		a, b, c, n = n, c, b-q*c, r
	}
	if a == 1 {
		if b < 0 {
			return b + m
		}
		return b
	}
	panic("Not invertible")
}

func main() {
	defer flush()

	T := readInt()
	for i := 0; i < T; i++ {
		N := readInt()
		S := readInt()
		K := readInt()
		d := gcd(gcd(K, -S), N)
		k := K / d
		n := N / d
		if gcd(k, n) != 1 {
			println(-1)
		} else {
			println(mod(invmod(k, n)*div(-S, d), n))
		}
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
