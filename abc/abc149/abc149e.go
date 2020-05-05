package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	N := readInt()
	M := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	sort.Sort(sort.Reverse(sort.IntSlice(A)))
	LB := A[N-1] * 2 // 一回の握手で上がる幸福度の下限は、左手も右手もパワーが一番低い人を握った場合
	UB := A[0] * 2   // 一回の握手で上がる幸福度の上限は、左手も右手もパワーが一番高い人を握った場合

	// cgs[i] は パワーがi以上のゲストの数
	cgs := make([]int, UB+1)
	for _, a := range A {
		cgs[a]++
	}
	for i := UB; i > 0; i-- {
		cgs[i-1] += cgs[i]
	}

	// 組み合わせの数がM以上になる一回で発生する幸福度の閾値を二分探索する
	isOk := func(n int) bool {
		m := 0
		for _, a := range A {
			m += cgs[max(n-a, 0)]
		}
		return m >= M
	}

	ok := LB
	ng := UB + 1
	for ng-ok != 1 {
		m := ok + (ng-ok)/2
		if isOk(m) {
			ok = m
		} else {
			ng = m
		}
	}

	// cps[i] は A[0]～A[i] の累積和
	cps := make([]int, N)
	cps[0] = A[0]
	for i := 1; i < N; i++ {
		cps[i] = A[i] + cps[i-1]
	}

	result := 0
	for _, a := range A {
		guests := cgs[max(ok-a, 0)]
		if guests != 0 {
			result += a*guests + cps[guests-1]
			M -= guests
		}
	}
	result += ok * M
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
