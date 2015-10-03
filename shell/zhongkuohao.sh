#!/bin/bash
# '[[' '[' 可以用于算术比较，字符串比较
# 只要用了"<"、">"，就表示是字符串比较，那么9 > 100为真，因为这实际上等价于‘9’ > ‘100’
# 鉴于以上情况，用算术比较，直接用let ,或者 (())

[ 20 -gt 10 ] && echo "err"
[[ 20 -gt 10 ]] && echo "err"
[[ 20 > 10 ]] && echo " [[ ok "
[ 20 \> 10 ] && echo " [ ok "

# 简单的模式匹配 注意等号右端的模式不能用引号括起，使用引用关闭了某些元字符的特殊功能
[ "test" = t..t ] && echo "match"

# if it's logic express, [[ use &&, [ use -a
[ 3 > 2 -a 5 > 4 ] && echo "right"
[[ 3 > 2 && 5 > 4 ]] && echo "right"

# for some operation, [ can use "", [[ can't use ""
[ -z "" ] && echo "[ zero"
[ "-z" "" ] && echo "[ "-z" zeor"
[ "-z" "" ] && echo "[ \"-z\" zeor"
[[ -z "" ]] && echo "[[ zero"
# wrong [[ "-z" "" ]] && echo "[[ zero"

#  [[ ... ]]进行算术扩展，而[ ... ]不做
[[ 99+1 -eq 100 ]] && echo "[[ expand equal"
# wrong [ 99+1 -eq 100 ] && echo "[ expand equal"
[ $((99+1)) -eq 100 ] && echo "[ expand equal"

# =~ is regular matching expression
