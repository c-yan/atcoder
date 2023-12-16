package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func main() {
	var n int
	fmt.Scanln(&n)
	var sc = bufio.NewScanner(os.Stdin)
	sc.Split(bufio.ScanWords)
	pt, px, py := 0, 0, 0
	for i := 0; i < n; i++ {
		sc.Scan()
		t, _ := strconv.Atoi(sc.Text())
		sc.Scan()
		x, _ := strconv.Atoi(sc.Text())
		sc.Scan()
		y, _ := strconv.Atoi(sc.Text())
		rt := (t - pt) - (Abs(x-px) + Abs(y-py))
		if rt < 0 || rt%2 != 0 {
			fmt.Println("No")
			return
		}
		pt, px, py = t, x, y
	}
	fmt.Println("Yes")
}
