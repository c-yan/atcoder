package main

import (
	"bufio"
	"fmt"
	"os"
)

func reverseString(s string) string {
	t := make([]byte, len(s))
	for i, b := range []byte(s) {
		t[len(s)-1-i] = b
	}
	return string(t)
}

func main() {
	s := readString()
	t := readString()
	dp := make([][]int, len(s)+1)
	for i := 0; i <= len(s); i++ {
		dp[i] = make([]int, len(t)+1)
	}
	for i := 1; i <= len(s); i++ {
		for j := 1; j <= len(t); j++ {
			k := dp[i-1][j]
			if dp[i][j-1] > k {
				k = dp[i][j-1]
			}
			if s[i-1] == t[j-1] && dp[i-1][j-1]+1 > k {
				k = dp[i-1][j-1] + 1
			}
			dp[i][j] = k
		}
	}
	u := make([]byte, 0, 4096)
	i := len(s)
	j := len(t)
	for i > 0 && j > 0 {
		if dp[i-1][j] == dp[i][j] {
			i--
		} else if dp[i][j-1] == dp[i][j] {
			j--
		} else {
			u = append(u, s[i-1])
			i--
			j--
		}
	}
	fmt.Println(reverseString(string(u)))
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
