package main

import (
	"bufio"
	"fmt"
	"math/big"
	"os"
	"strconv"
)

const (
	m = 1000000007
)

func main() {
	N := readInt()
	A := make([]*big.Int, N)
	for i := 0; i < N; i++ {
		A[i] = big.NewInt(int64(readInt()))
	}

	t := new(big.Int)

	lcm := big.NewInt(1)
	for i := 0; i < N; i++ {
		t.GCD(nil, nil, lcm, A[i])
		lcm.Mul(lcm, A[i])
		lcm.Div(lcm, t)
	}

	result := big.NewInt(0)
	for i := 0; i < N; i++ {
		result.Add(result, t.Div(lcm, A[i]))
	}
	result.Rem(result, big.NewInt(m))

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
