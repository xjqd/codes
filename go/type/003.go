package main

import "fmt"

type Person struct {
	name string
}

func (p *Person) print() {
	fmt.Println(p.name)
}
func main() {
	l := Person{"sam"}
	l.print()
}
