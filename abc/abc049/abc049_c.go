package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var words = []string{"maerd", "remaerd", "esare", "resare"}

func reverseString(s string) string {
	t := make([]byte, len(s))
	for i, b := range []byte(s) {
		t[len(s)-1-i] = b
	}
	return string(t)
}

func main() {
	defer flush()

	S := readString()

	s := reverseString(S)
next:
	if s == "" {
		println("YES")
		return
	}
	for _, w := range words {
		if strings.HasPrefix(s, w) {
			s = s[len(w):]
			goto next
		}
	}
	println("NO")
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
