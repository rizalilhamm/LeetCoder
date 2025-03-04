package main

func isPowerOfFour(n int) bool {
    if n <= 0 {
        return false
    }

    for n > 1 {
        if n % 4 != 0 {
            return false
        }
        n /= 4
    }

    return n == 1
}