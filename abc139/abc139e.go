package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	N := readInt()
	a := make([][]int, N)
	for i := 0; i < N; i++ {
		a[i] = make([]int, N-1)
		for j := 0; j < N-1; j++ {
			a[i][j] = readInt() - 1
		}
	}

	nextIndex := make([]int, N)
	nextQueue := make([]int, 0, N)
	for i := 0; i < N; i++ {
		nextQueue = append(nextQueue, i)
	}
	result := 0
	finished := 0

	for len(nextQueue) > 0 {
		result++
		queue := nextQueue
		nextQueue = nil
		booked := make([]bool, N)
		for i := 0; i < len(queue); i++ {
			player := queue[i]
			if booked[player] {
				continue
			}
			opponent := a[player][nextIndex[player]]
			if booked[opponent] {
				continue
			}
			if a[opponent][nextIndex[opponent]] != player {
				continue
			}
			booked[player] = true
			booked[opponent] = true
			nextIndex[player]++
			nextIndex[opponent]++
			if nextIndex[player] == N-1 {
				finished++
			} else {
				nextQueue = append(nextQueue, player)
			}
			if nextIndex[opponent] == N-1 {
				finished++
			} else {
				nextQueue = append(nextQueue, opponent)
			}
		}
	}
	if finished == N {
		fmt.Println(result)
	} else {
		fmt.Println(-1)
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
