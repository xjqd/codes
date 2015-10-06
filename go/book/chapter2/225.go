package main

import (
	"errors"
	"fmt"
)

//func Add(x int, y int) (ret int, err error) {
func Add(x, y int) (ret int, err error) {
	if x < 0 || y < 0 {
		err = errors.New("should be non-negative values\n")
		return
	}
	return x + y, nil
}
func main() {
	sum, ok := Add(3, 4)
	fmt.Println(sum, ok)
}
