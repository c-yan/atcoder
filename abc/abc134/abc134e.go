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

type treapNode struct {
	value    int
	priority uint
	count    int
	left     *treapNode
	right    *treapNode
}

func newTreapNode(v int) *treapNode {
	return &treapNode{v, xorshift(), 1, nil, nil}
}

func treapRotateRight(n *treapNode) *treapNode {
	l := n.left
	n.left = l.right
	l.right = n
	return l
}

func treapRotateLeft(n *treapNode) *treapNode {
	r := n.right
	n.right = r.left
	r.left = n
	return r
}

func treapInsert(n *treapNode, v int) *treapNode {
	if n == nil {
		return newTreapNode(v)
	}
	if n.value == v {
		n.count++
		return n
	}
	if n.value > v {
		n.left = treapInsert(n.left, v)
		if n.priority > n.left.priority {
			n = treapRotateRight(n)
		}
	} else {
		n.right = treapInsert(n.right, v)
		if n.priority > n.right.priority {
			n = treapRotateLeft(n)
		}
	}
	return n
}

func treapDelete(n *treapNode, v int) *treapNode {
	if n == nil {
		return nil
	}
	if n.value > v {
		n.left = treapDelete(n.left, v)
		return n
	}
	if n.value < v {
		n.right = treapDelete(n.right, v)
		return n
	}

	// n.value == v
	if n.count > 1 {
		n.count--
		return n
	}

	if n.left == nil && n.right == nil {
		return nil
	}

	if n.left == nil {
		n = treapRotateLeft(n)
	} else if n.right == nil {
		n = treapRotateRight(n)
	} else {
		// n.left != nil && n.right != nil
		if n.left.priority < n.right.priority {
			n = treapRotateRight(n)
		} else {
			n = treapRotateLeft(n)
		}
	}
	return treapDelete(n, v)
}

func treapCount(n *treapNode) int {
	if n == nil {
		return 0
	}
	return n.count + treapCount(n.left) + treapCount(n.right)
}

func treapString(n *treapNode) string {
	if n == nil {
		return ""
	}
	result := make([]string, 0)
	if n.left != nil {
		result = append(result, treapString(n.left))
	}
	result = append(result, fmt.Sprintf("%d:%d", n.value, n.count))
	if n.right != nil {
		result = append(result, treapString(n.right))
	}
	return strings.Join(result, " ")
}

// v 未満で最大のノードを検索する. v 未満のノードがなければ nil を返す
func treapSearch(n *treapNode, v int) *treapNode {
	if n == nil {
		return nil
	}
	if n.value >= v {
		if n.left == nil {
			return nil
		}
		return treapSearch(n.left, v)
	}
	// n.value < v
	if n.right == nil {
		return n
	}
	r := treapSearch(n.right, v)
	if r == nil {
		return n
	}
	return r
}

type treap struct {
	root *treapNode
}

func (t *treap) Insert(v int) {
	t.root = treapInsert(t.root, v)
}

func (t *treap) Delete(v int) {
	t.root = treapDelete(t.root, v)
}

func (t *treap) String() string {
	return treapString(t.root)
}

func (t *treap) Count() int {
	return treapCount(t.root)
}

func (t *treap) Search(v int) *treapNode {
	return treapSearch(t.root, v)
}

func main() {
	defer flush()

	N := readInt()
	A := make([]int, N)
	for i := 0; i < N; i++ {
		A[i] = readInt()
	}

	t := &treap{}
	for i := 0; i < N; i++ {
		a := A[i]
		n := t.Search(a)
		if n != nil {
			//printf("delete: %d\n", n.value)
			t.Delete(n.value)
		}
		//printf("insert: %d\n", a)
		t.Insert(a)
		//printf("result: %s\n", t)
	}
	println(t.Count())
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
