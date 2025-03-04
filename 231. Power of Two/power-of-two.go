package main

func isPowerOfTwo(n int) bool {
    if n <= 0 {
        return false
    }
    resp := 0
    idx := 0

    for resp <= n {
        if resp == n {
            return true
        }
        
        resp = pow(2, idx)
        idx += 1
    }
    return false
}

func pow(base, exponent int) int {
    res := 1

    for i := 0; i < exponent; i++ {
        res *= base
    }
    return res
}