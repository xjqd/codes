package main

import "fmt"

type Person struct {
	name string
}

func (p *Person) print() {
	fmt.Println(p.name)
}

func (p Person) print() {
	fmt.Println(p.name)
}

func main() {
	fmt.Println("hello")
}
