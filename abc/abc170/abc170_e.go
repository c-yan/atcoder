// 平衡二分探索木
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
		panic("node is not found!")
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

func treapMin(n *treapNode) int {
	if n.left != nil {
		return treapMin(n.left)
	}
	return n.value
}

func treapMax(n *treapNode) int {
	if n.right != nil {
		return treapMax(n.right)
	}
	return n.value
}

type treap struct {
	root *treapNode
	size int
}

func (t *treap) Insert(v int) {
	t.root = treapInsert(t.root, v)
	t.size++
}

func (t *treap) Delete(v int) {
	t.root = treapDelete(t.root, v)
	t.size--
}

func (t *treap) String() string {
	return treapString(t.root)
}

func (t *treap) Count() int {
	return t.size
}

func (t *treap) Min() int {
	return treapMin(t.root)
}

func (t *treap) Max() int {
	return treapMax(t.root)
}

func main() {
	defer flush()

	N := readInt()
	Q := readInt()

	maxRatings := &treap{}
	kindergartens := make([]*treap, 200001)
	for i := 0; i < 200001; i++ {
		kindergartens[i] = &treap{}
	}
	ratings := make([]int, N+1)
	belongs := make([]int, N+1)

	for i := 1; i < N+1; i++ {
		A := readInt()
		B := readInt()
		ratings[i] = A
		belongs[i] = B
		kindergartens[B].Insert(A)
	}

	for i := 1; i < 200001; i++ {
		if kindergartens[i].Count() != 0 {
			maxRatings.Insert(kindergartens[i].Max())
		}
	}

	for i := 0; i < Q; i++ {
		C := readInt()
		D := readInt()

		from := kindergartens[belongs[C]]
		to := kindergartens[D]
		rating := ratings[C]
		belongs[C] = D

		maxRatings.Delete(from.Max())
		from.Delete(rating)
		if from.Count() != 0 {
			maxRatings.Insert(from.Max())
		}

		if to.Count() != 0 {
			maxRatings.Delete(to.Max())
		}
		to.Insert(rating)
		maxRatings.Insert(to.Max())

		println(maxRatings.Min())
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
