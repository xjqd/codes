package main

import "fmt"

func sum(a []int, c chan int) {
	sum := 0
	for _, v := range a {
		sum += v
	}
	fmt.Println(" exec sum ")
	c <- sum
	fmt.Println(" sum done")
}

func main() {
	a := []int{7, 2, 8, -9, 4, 0}
	c := make(chan int)
	go sum(a[:len(a)/2], c)
	fmt.Println("second part")
	go sum(a[len(a)/2:], c)
	fmt.Println("second part done")
	//	x, y := <-c, <-c
	x := <-c
	fmt.Println(" extract y ")
	y := <-c
	fmt.Println(x, y, x+y)
}
