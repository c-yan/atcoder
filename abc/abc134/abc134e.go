package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	y uint = 88172645463325252
)

func xorshift() uint {
	y ^= y << 7
	y ^= y >> 9
	return y
}

type node struct {
	value    int
	priority uint
	count    int
	left     *node
	right    *node
}

func newNode(x int) *node {
	return &node{x, xorshift(), 1, nil, nil}
}

func rotateRight(n *node) *node {
	l := n.left
	n.left = l.right
	l.right = n
	return l
}

func rotateLeft(n *node) *node {
	r := n.right
	n.right = r.left
	r.left = n
	return r
}

func insert(n *node, x int) *node {
	if n == nil {
		return newNode(x)
	}
	if x == n.value {
		n.count++
		return n
	}
	if x < n.value {
		n.left = insert(n.left, x)
		if n.priority > n.left.priority {
			n = rotateRight(n)
		}
	} else {
		n.right = insert(n.right, x)
		if n.priority > n.right.priority {
			n = rotateLeft(n)
		}
	}
	return n
}

func delete(n *node, x int) *node {
	if n == nil {
		return nil
	}
	if n.value > x {
		n.left = delete(n.left, x)
		return n
	}
	if n.value < x {
		n.right = delete(n.right, x)
		return n
	}

	// n.value == x
	if n.count > 1 {
		n.count--
		return n
	}

	if n.left == nil && n.right == nil {
		return nil
	}

	if n.left == nil {
		n = rotateLeft(n)
	} else if n.right == nil {
		n = rotateRight(n)
	} else {
		// n.left != nil && n.right != nil
		if n.left.priority < n.right.priority {
			n = rotateRight(n)
		} else {
			n = rotateLeft(n)
		}
	}
	return delete(n, x)
}

func size(n *node) int {
	if n == nil {
		return 0
	}
	return n.count + size(n.left) + size(n.right)
}

func str(n *node) string {
	if n == nil {
		return ""
	}
	result := make([]string, 0)
	if n.left != nil {
		result = append(result, str(n.left))
	}
	result = append(result, fmt.Sprintf("%d:%d", n.value, n.count))
	if n.right != nil {
		result = append(result, str(n.right))
	}
	return strings.Join(result, " ")
}

// x 未満で最大のノードを検索する. n 未満のノードがなければ nil を返す
func search(n *node, x int) *node {
	if n == nil {
		return nil
	}
	if n.value >= x {
		if n.left == nil {
			return nil
		}
		return search(n.left, x)
	}
	// n.value < x
	if n.right == nil {
		return n
	}
	r := search(n.right, x)
	if r == nil {
		return n
	}
	return r
}

func main() {
	defer flush()

	N := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	var n *node
	for i := 0; i < N; i++ {
		a := A[i]
		t := search(n, a)
		if t != nil {
			//printf("delete: %d\n", t.value)
			n = delete(n, t.value)
		}
		//printf("insert: %d\n", a)
		n = insert(n, a)
		//printf("result: %s\n", str(n))
	}
	println(size(n))
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

func readInts(n int) []int {
	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = readInt()
	}
	return result
}

var stdoutWriter = bufio.NewWriter(os.Stdout)

func flush() {
	stdoutWriter.Flush()
}

func printf(f string, args ...interface{}) (int, error) {
	return fmt.Fprintf(stdoutWriter, f, args...)
}

func println(args ...interface{}) (int, error) {
	return fmt.Fprintln(stdoutWriter, args...)
}
