package main

import (
	"fmt"
)

type Vector []float64

func (v Vector) DoSome(i, n int, u Vector, c chan int) {
	for ; i < n; i++ {
		v[i] += u.Op(v[i])
	}
	c <- 1
}

func (v Vector) Op(m float64) (n float64) {
	return m * m
}

const NCPU = 16

func (v Vector) DoAll(u Vector) {
	c := make(chan int, NCPU)
	for i := 0; i < NCPU; i++ {
		go v.DoSome(i*len(v)/NCPU, (i+1)*len(v)/NCPU, u, c)
	}

	for i := 0; i < NCPU; i++ {
		<-c
	}
}

func main() {
	var vect = Vector{1, 2, 3, 4, 5, 6, 7, 8.9, 10, 1, 1, 4, 5, 6}
	var vectU = Vector{1, 2, 3, 4, 5, 6, 7, 8.9, 10, 1, 1, 4, 5, 6}
	vect.DoAll(vectU)
	fmt.Println(vect)
	fmt.Println(vectU)
}
