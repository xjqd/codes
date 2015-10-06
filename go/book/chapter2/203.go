package main

func main() {
	var val1 int32
	val2 := 64
	val1 = int32(val2)
	/*./203.go:6: cannot use val2 (type int) as type int32 in assignment */
}
