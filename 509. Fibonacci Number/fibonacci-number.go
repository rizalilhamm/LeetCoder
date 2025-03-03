package main

func fib(n int) int {

    if n < 1 {
        return 0
    }
    prev, curr := 0, 1
    var temp int

    for i := 1; i < n; i++ {
        temp = curr
        curr = prev + curr
        prev = temp
    }

    return curr
}


// 1, 2, 3,5 , 8, 13, 21, 34, 545