package main

import "fmt"

func main() {
	str := "hello world"
	n := len(str)
	/* expected '}', found 'EOF'
	for (i := 0; i < n; i++) { */
	for i := 0; i < n; i++ {
		fmt.Println(i, str[i])
	}
	for i, ch := range str {
		fmt.Println(i, ch)
	}
}
