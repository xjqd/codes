#!/bin/bash
E_NOSUCHFILE=65

read -p "File name:" file
if [ ! -e $file ]
 then
    echo "$file is not existed"
    exit $E_NOSUCHFILE
fi

read -p "Title: " title
cat - $file <<< "$title" >${file}.new
echo "Modfied file is ${file}.new"
exit 0
