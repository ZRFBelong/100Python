#!/bin/bash

for i in {1..100}  # 更改这里的括号和逗号为花括号并去掉i++
do
    if touch "100-$i.py"
    then
        echo "100-$i.py file created"
    fi
done
