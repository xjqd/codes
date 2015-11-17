package main

import "fmt"

func main() {
	var uid int32 = 12345
	var gid int64 = int64(uid)
	fmt.Println(uid)
	fmt.Println(gid)
}
