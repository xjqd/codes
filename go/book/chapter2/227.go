package main

import (
	"fmt"
	"prin"
	"prin/hello"
)

func main() {
	ret, ok := prin.Sub(3, 7)
	fmt.Println(ret, ok)
	hello.Hello("abc")
	hello.Abc()
}
