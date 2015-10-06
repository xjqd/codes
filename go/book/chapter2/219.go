package main

import "fmt"

func main() {

	type person struct {
		name string
		age  int
	}

	//var groups = map[string]person
	//var groups["abc"] = map[string]person{"jian", 35}
	var groups = map[string]person{}
	//var groups map[string]person
	groups["team1"] = person{"sam", 30}
	org := make(map[string]person, 10)
	org["mgc8"] = person{"niu", 5}

	name, age := org["mgc8"]

	if age {
		fmt.Println("find the age", age)

	} else {
		fmt.Println("find the name", name)
	}
	groups["1234"] = person{"jian", 35}

	fmt.Println(groups)
	fmt.Println(org)
	delete(groups, "nil")
	delete(groups, "")
	delete(groups, "1234")
	fmt.Println(groups)
	p1, ok := groups["team1"]
	if ok {
		fmt.Println("find", p1)
	} else {
		fmt.Println("not find")
	}
}
