package main

import "fmt"
import "one"
import "two"

type Integer int

func (a Integer) Read([]byte) int {
	return 10
}
func (a Integer) Write([]byte) int {
	return 11
}

func main() {
	var r one.ReadWrite = new(Integer)
	var s two.Istream = new(Integer)
	var t two.Istream = r
	var m two.Saction = s
	/*
	   var n one.ReadWrite = m
	    cannot use m (type two.Saction) as type one.ReadWrite in assignment:
	            two.Saction does not implement one.ReadWrite (missing Read method)
	*/
	fmt.Println(r)
	fmt.Println(s)
	fmt.Println(t)
	fmt.Println(m)
	var x one.Read = t
	fmt.Println(x)
	y, ok := x.(one.ReadWrite)
	if ok {
		fmt.Println("in the range", y, ok)
	}
	//a, ok := m.(two.Istream)
	//a, ok := m.(Integer)
	//a, ok := m.(one.ReadWrite)
	a, ok := m.(two.Saction)
	if ok {
		fmt.Println(" for m= ", m)
		fmt.Println(" for a= ", a)
	}
}
