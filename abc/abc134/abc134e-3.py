from random import random
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


class TreapNode:
    _value = None
    _priority = None
    _count = None
    _left = None
    _right = None

    def __init__(self, value):
        self._value = value
        self._priority = random()
        self._count = 1


def treap_rotate_right(n):
    l = n._left
    n._left = l._right
    l._right = n
    return l


def treap_rotate_left(n):
    r = n._right
    n._right = r._left
    r._left = n
    return r


def treap_insert(n, v):
    if n is None:
        return TreapNode(v)
    if n._value == v:
        n._count += 1
        return n
    if n._value > v:
        n._left = treap_insert(n._left, v)
        if n._priority > n._left._priority:
            n = treap_rotate_right(n)
    else:
        n._right = treap_insert(n._right, v)
        if n._priority > n._right._priority:
            n = treap_rotate_left(n)
    return n


def treap_delete(n, v):
    if n is None:
        raise Exception('no nodes')
    if n._value > v:
        n._left = treap_delete(n._left, v)
        return n
    if n._value < v:
        n._right = treap_delete(n._right, v)
        return n

    # n._value == v
    if n._count > 1:
        n._count -= 1
        return n

    if n._left is None and n._right is None:
        return None

    if n._left is None:
        n = treap_rotate_left(n)
    elif n._right is None:
        n = treap_rotate_right(n)
    else:
        # n._left is not None and n._right is not None
        if n._left._priority < n._right._priority:
            n = treap_rotate_right(n)
        else:
            n = treap_rotate_left(n)
    return treap_delete(n, v)


def treap_size(n):
    if n is None:
        return 0
    return n._count + treap_size(n._left) + treap_size(n._right)


def treap_str(n):
    if n is None:
        return ""
    result = []
    if n._left is not None:
        result.append(treap_str(n._left))
    result.append("%d:%d" % (n._value, n._count))
    if n._right is not None:
        result.append(treap_str(n._right))
    return ' '.join(result)


def treap_search(n, v):
    # v 未満で最大のノードを検索する. v 未満のノードがなければ None を返す
    if n is None:
        return None
    if n._value >= v:
        if n._left is None:
            return None
        return treap_search(n._left, v)
    # n._value < v
    if n._right is None:
        return n
    r = treap_search(n._right, v)
    if r is None:
        return n
    return r


class Treap:
    _root = None
    _size = 0

    def insert(self, v):
        self._root = treap_insert(self._root, v)
        self._size += 1

    def delete(self, v):
        self._root = treap_delete(self._root, v)
        self._size -= 1

    def __len__(self):
        return self._size

    def __str__(self):
        return treap_str(self._root)

    def search(self, v):
        return treap_search(self._root, v)


N = int(input())
A = [int(input()) for _ in range(N)]

t = Treap()
for a in A:
    n = t.search(a)
    if n is not None:
        t.delete(n._value)
    t.insert(a)
print(len(t))
