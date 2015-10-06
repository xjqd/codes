package checkerror

import (
	//"errors"
	"fmt"
	"os"
)

func CheckError(err error) {
	if err != nil {
		fmt.Println("Fatal error: ", err.Error())
		os.Exit(1)
	}
}
