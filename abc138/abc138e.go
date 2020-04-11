package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	s := readString()
	t := readString()

	available := make([]bool, 26)
	for _, b := range []byte(s) {
		available[b-'a'] = true
	}
	for _, b := range []byte(t) {
		if !available[b-'a'] {
			fmt.Println(-1)
			return
		}
	}

	lut := make([][]int, 26)
	s2 := []byte(s + s)
	for i := range available {
		if !available[i] {
			continue
		}
		lut[i] = make([]int, len(s))
		j := 0
		for k := len(s2) - 1; k >= 0; k-- {
			if int(s2[k]) == i+'a' {
				j = 0
			} else {
				j++
			}
			if i < len(s) {
				lut[i][k] = j
			}
		}
	}

	i := 0
	for _, b := range []byte(t) {
		i += lut[b-'a'][i%len(s)] + 1
	}
	fmt.Println(i)
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
