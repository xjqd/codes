package main

import "fmt"

type Base struct {
	x, y int
}

func (b Base) Bar() {
	fmt.Println("Base:Bar")
}
func (b Base) Foo() {
	fmt.Println("Base:Foo")
}

type Foo struct {
	m, n float64
	*Base
}

func (f Foo) Bar() {
	fmt.Println("Foo:Bar")
}
func main() {
	// Base literal is not a type
	//b := new(Base{10, 20})
	//b := &Base{10, 20}
	b := new(Base)
	//f := new(Foo{Base{30, 40}, 16.6, 18.8})
	f := &Foo{16.6, 18.8, &Base{10, 20}}
	b.Bar()
	b.Foo()
	f.Bar()
	f.Foo()
}
