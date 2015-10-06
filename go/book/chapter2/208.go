package main

import "fmt"

func main() {
	var str string = "hello world"
	var str1 string = "world" + "hello"
	ch := str[0]
	//str[0] = 'M'
	fmt.Printf("ch=%c\n", ch)
	fmt.Printf("str1=%s\n", str1)
	fmt.Printf("str=%s len=%d\n", str, len(str))
}
