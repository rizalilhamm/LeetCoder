package main

func isPowerOfThree(n int) bool {
    if n <= 0 {
        return false
    }

    res, idx := 0, 0
    for res < n {
        if res == n {
            return true
        }
        res = power(3, idx)
        idx += 1
    }
    return res == n
}

func power(base, exponent int) int {
    var result int = 1

    for i := 0; i < exponent; i++ {
        result *= base
    }
    return result
}