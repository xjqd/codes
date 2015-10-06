package main

import "fmt"

func main() {

	//var mystr  struct person{
	type B struct {
		name string
		age  int
	}
	type person struct {
		//	b    B
		B
		name string
		age  int
		mail string
	}
	/*
	   struct A {
	   name string
	   age int
	   }
	*/
	//var mystr = person{B{"ab", 20},sam", 10, "xue"}
	mystr := person{B{"ab", 20}, "sam", 10, "xue"}

	//fmt.Println(mystr.b.name)
	fmt.Println(mystr.B.name)
}
