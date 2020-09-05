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
	key      int
	value    int
	priority uint
	left     *treapNode
	right    *treapNode
}

func newTreapNode(k int, v int) *treapNode {
	return &treapNode{k, v, xorshift(), nil, nil}
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

func treapFind(n *treapNode, k int) *treapNode {
	if n == nil {
		return nil
	}
	if n.key == k {
		return n
	}
	if n.key > k {
		return treapFind(n.left, k)
	}
	return treapFind(n.right, k)
}

func treapLowerBound(n *treapNode, k int) *treapNode {
	if n == nil {
		return nil
	}
	if n.key < k {
		return treapLowerBound(n.right, k)
	}
	if t := treapLowerBound(n.left, k); t != nil {
		return t
	}
	return n
}

func treapInsert(n *treapNode, k int, v int) *treapNode {
	if n == nil {
		return newTreapNode(k, v)
	}
	if n.key == k {
		panic("node key is duplicated!")
	}
	if n.key > k {
		n.left = treapInsert(n.left, k, v)
		if n.priority > n.left.priority {
			n = treapRotateRight(n)
		}
	} else {
		n.right = treapInsert(n.right, k, v)
		if n.priority > n.right.priority {
			n = treapRotateLeft(n)
		}
	}
	return n
}

func treapDelete(n *treapNode, k int) *treapNode {
	if n == nil {
		panic("node is not found!")
	}
	if n.key > k {
		n.left = treapDelete(n.left, k)
		return n
	}
	if n.key < k {
		n.right = treapDelete(n.right, k)
		return n
	}

	// n.key == k
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
	return treapDelete(n, k)
}

func treapCount(n *treapNode) int {
	if n == nil {
		return 0
	}
	return 1 + treapCount(n.left) + treapCount(n.right)
}

func treapString(n *treapNode) string {
	if n == nil {
		return ""
	}
	result := make([]string, 0)
	if n.left != nil {
		result = append(result, treapString(n.left))
	}
	result = append(result, fmt.Sprintf("%d:%d", n.key, n.value))
	if n.right != nil {
		result = append(result, treapString(n.right))
	}
	return strings.Join(result, " ")
}

func treapMin(n *treapNode) int {
	if n == nil {
		panic("node is not found!")
	}
	if n.left != nil {
		return treapMin(n.left)
	}
	return n.key
}

func treapMax(n *treapNode) int {
	if n == nil {
		panic("node is not found!")
	}
	if n.right != nil {
		return treapMax(n.right)
	}
	return n.key
}

type treap struct {
	root *treapNode
	size int
}

func (t *treap) Find(k int) *treapNode {
	return treapFind(t.root, k)
}

func (t *treap) LowerBound(k int) *treapNode {
	return treapLowerBound(t.root, k)
}

func (t *treap) Insert(k int, v int) {
	t.root = treapInsert(t.root, k, v)
	t.size++
}

func (t *treap) Delete(k int) {
	t.root = treapDelete(t.root, k)
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

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func main() {
	defer flush()

	H := readInt()
	W := readInt()

	candidates := &treap{}
	moves := &treap{}

	for i := 0; i < W; i++ {
		candidates.Insert(i, i)
	}
	moves.Insert(0, W)

	for i := 0; i < H; i++ {
		A := readInt() - 1
		B := readInt()

		r := -1
		for {
			n := candidates.LowerBound(A)
			if n == nil || n.key > B {
				break
			}
			r = max(r, n.value)
			t := moves.Find(n.key - n.value)
			t.value--
			if t.value == 0 {
				moves.Delete(t.key)
			}
			candidates.Delete(n.key)
		}

		if r != -1 && B != W {
			t := B - r
			n := moves.Find(t)
			if n == nil {
				moves.Insert(t, 1)
			} else {
				n.value++
			}
			candidates.Insert(B, r)
		}

		if moves.Count() == 0 {
			println(-1)
		} else {
			println(moves.Min() + i + 1)
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
