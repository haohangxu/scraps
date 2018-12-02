#!/bin/bash

process1 () {
    sleep 10
    echo "process 1 done"
}

process2 () {
    sleep 5
    echo "process 2 done"
}

background () {
    $1 &
    wait $! && echo "$2"
}

( background process1 "process 1 has finished" ) &
( background process2 "process 2 has finished" ) &

wait
